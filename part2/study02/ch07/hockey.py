"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import columns
import thinkbayes
import thinkstats
import thinkplot


USE_SUMMARY_DATA = True
        

class Hockey(thinkbayes.Suite):
    """Represents hypotheses about the scoring rate for a team."""

    def __init__(self, name=''):
        """Initializes the Hockey object.

        name: string
        """
        if USE_SUMMARY_DATA:
            # prior based on each team's average goals scored
            mu = 2.7
            sigma = 0.3
        else:
            # prior based on each pair-wise match-up
            mu = 2.7
            sigma = 0.85

        pmf = thinkbayes.MakeGaussianPmf(mu, sigma, 4)
        
        
        thinkbayes.Suite.__init__(self, pmf, name=name)

  def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        Evaluates the Poisson PMF for lambda and k.

        hypo: goal scoring rate in goals per game
        data: goals scored in one period
        """
        lam = hypo
        k = data
        like = thinkbayes.EvalPoissonPmf(k, lam)
        return like
    
def MakeGoalPmf(suite, high=10):
    """Makes the distribution of goals scored, given distribution of lam.

    suite: distribution of goal-scoring rate
    high: upper bound

    returns: Pmf of goals per game
    """
    metapmf = thinkbayes.Pmf()

    for lam, prob in suite.Items():
        pmf = thinkbayes.MakePoissonPmf(lam, high)
        metapmf.Set(pmf, prob)

    mix = thinkbayes.MakeMixture(metapmf, name=suite.name)
    return mix


def MakeGoalTimePmf(suite):
    """Makes the distribution of time til first goal.

    suite: distribution of goal-scoring rate

    returns: Pmf of goals per game
    """
    metapmf = thinkbayes.Pmf()

    for lam, prob in suite.Items():
        pmf = thinkbayes.MakeExponentialPmf(lam, high=2, n=2001)
        metapmf.Set(pmf, prob)

    mix = thinkbayes.MakeMixture(metapmf, name=suite.name)
    return mix

class Game(object):
    """Represents a game.

    Attributes are set in columns.read_csv.
    """
    convert = dict()

    def clean(self):
        self.goals = self.pd1 + self.pd2 + self.pd3


def ReadHockeyData(filename='hockey_data.csv'):
    """Read game scores from the data file.

    filename: string
    """
    game_list = columns.read_csv(filename, Game)

    # map from gameID to list of two games
    games = {}
    for game in game_list:
        if game.season != 2011:
            continue
        key = game.game
        games.setdefault(key, []).append(game)

    # map from (team1, team2) to (score1, score2)
    pairs = {}
    for key, pair in games.iteritems():
        t1, t2 = pair
        key = t1.team, t2.team
        entry = t1.total, t2.total
        pairs.setdefault(key, []).append(entry)

    ProcessScoresTeamwise(pairs)
    ProcessScoresPairwise(pairs)


def ProcessScoresPairwise(pairs):
    """Average number of goals for each team against each opponent.

    pairs: map from (team1, team2) to (score1, score2)
    """
    # map from (team1, team2) to list of goals scored
    goals_scored = {}
    for key, entries in pairs.iteritems():
        t1, t2 = key
        for entry in entries:
            g1, g2 = entry
            goals_scored.setdefault((t1, t2), []).append(g1)
            goals_scored.setdefault((t2, t1), []).append(g2)

    # make a list of average goals scored
    lams = []
    for key, goals in goals_scored.iteritems():
        if len(goals) < 3:
            continue
        lam = thinkstats.Mean(goals)
        lams.append(lam)

    # make the distribution of average goals scored
    cdf = thinkbayes.MakeCdfFromList(lams)
    thinkplot.Cdf(cdf)
    thinkplot.Show()

    mu, var = thinkstats.MeanVar(lams)
    print 'mu, sig', mu, math.sqrt(var)

    print 'BOS v VAN', pairs['BOS', 'VAN']


def ProcessScoresTeamwise(pairs):
    """Average number of goals for each team.

    pairs: map from (team1, team2) to (score1, score2)
    """
    # map from team to list of goals scored
    goals_scored = {}
    for key, entries in pairs.iteritems():
        t1, t2 = key
        for entry in entries:
            g1, g2 = entry
            goals_scored.setdefault(t1, []).append(g1)
            goals_scored.setdefault(t2, []).append(g2)

    # make a list of average goals scored
    lams = []
    for key, goals in goals_scored.iteritems():
        lam = thinkstats.Mean(goals)
        lams.append(lam)

    # make the distribution of average goals scored
    cdf = thinkbayes.MakeCdfFromList(lams)
    thinkplot.Cdf(cdf)
    thinkplot.Show()

    mu, var = thinkstats.MeanVar(lams)
    print 'mu, sig', mu, math.sqrt(var)


def main():
    #ReadHockeyData()
    #return

    formats = ['pdf', 'eps']

    suite1 = Hockey('bruins')
    suite2 = Hockey('canucks')

    thinkplot.Clf()
    thinkplot.PrePlot(num=2)
    thinkplot.Pmf(suite1)
    thinkplot.Pmf(suite2)
    thinkplot.Save(root='hockey0',
                xlabel='Goals per game',
                ylabel='Probability',
                formats=formats)

    suite1.UpdateSet([0, 2, 8, 4])
    suite2.UpdateSet([1, 3, 1, 0])

    thinkplot.Clf()
    thinkplot.PrePlot(num=2)
    thinkplot.Pmf(suite1)
    thinkplot.Pmf(suite2)
    thinkplot.Save(root='hockey1',
                xlabel='Goals per game',
                ylabel='Probability',
                formats=formats)


    goal_dist1 = MakeGoalPmf(suite1)
    goal_dist2 = MakeGoalPmf(suite2)

    thinkplot.Clf()
    thinkplot.PrePlot(num=2)
    thinkplot.Pmf(goal_dist1)
    thinkplot.Pmf(goal_dist2)
    thinkplot.Save(root='hockey2',
                xlabel='Goals',
                ylabel='Probability',
                formats=formats)

    time_dist1 = MakeGoalTimePmf(suite1)    
    time_dist2 = MakeGoalTimePmf(suite2)
 
    print 'MLE bruins', suite1.MaximumLikelihood()
    print 'MLE canucks', suite2.MaximumLikelihood()
   
    thinkplot.Clf()
    thinkplot.PrePlot(num=2)
    thinkplot.Pmf(time_dist1)
    thinkplot.Pmf(time_dist2)    
    thinkplot.Save(root='hockey3',
                   xlabel='Games until goal',
                   ylabel='Probability',
                   formats=formats)

if __name__ == '__main__':
    main()