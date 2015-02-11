


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>bayesianWork/python_install_guide.md at master · psygrammer/bayesianWork</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="psygrammer/bayesianWork" name="twitter:title" /><meta content="Contribute to bayesianWork development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/8865010?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/8865010?v=3&amp;s=400" property="og:image" /><meta content="psygrammer/bayesianWork" property="og:title" /><meta content="https://github.com/psygrammer/bayesianWork" property="og:url" /><meta content="Contribute to bayesianWork development by creating an account on GitHub." property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="D2D95FFD:12AE:380A7A7:54DADD07" name="octolytics-dimension-request_id" /><meta content="1955312" name="octolytics-actor-id" /><meta content="mooithub" name="octolytics-actor-login" /><meta content="f35b1987f128b63404a4d5d9d26d8f792c961c14194200271f5e36eab49d4a8c" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="o9Z7w/kjciOxKsMFEdQR4ppTh43PQxQ29Snv5D9nWY6H9oUYeoOfwhx0GybMlR0J/CqGw4C0Lk/JABUF9+Tyjg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-a877311d38319215d5b12cc8009c0260e2e2935a87976dec85ee155bc865fe97.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-59560293230f3256c9ef81c352f7379d7413eee179a31d8206643660056323cd.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="7c222a1768233fd6716f44cf7aa6bc71">

      
  <meta name="description" content="Contribute to bayesianWork development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/psygrammer/bayesianWork git https://github.com/psygrammer/bayesianWork.git">

  <meta content="8865010" name="octolytics-dimension-user_id" /><meta content="psygrammer" name="octolytics-dimension-user_login" /><meta content="27693910" name="octolytics-dimension-repository_id" /><meta content="psygrammer/bayesianWork" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="27693910" name="octolytics-dimension-repository_network_root_id" /><meta content="psygrammer/bayesianWork" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/psygrammer/bayesianWork/commits/master.atom" rel="alternate" title="Recent Commits to bayesianWork:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production linux vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/psygrammer/bayesianWork/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/psygrammer/bayesianWork/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/mooithub" data-ga-click="Header, go to profile, text:username">
      <img alt="mooithub" class="avatar" data-user="1955312" height="20" src="https://avatars2.githubusercontent.com/u/1955312?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">mooithub</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>
    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="psygrammer">This organization</span>
    </li>

    <li>
      <a href="/orgs/psygrammer/invitations/new" data-ga-click="Header, invite someone, icon:person"><span class="octicon octicon-person"></span> Invite someone</a>
    </li>

    <li>
      <a href="/orgs/psygrammer/new-team" data-ga-click="Header, create new team, icon:jersey"><span class="octicon octicon-jersey"></span> New team</a>
    </li>

    <li>
      <a href="/organizations/psygrammer/repositories/new" data-ga-click="Header, create new organization repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
    </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="psygrammer/bayesianWork">This repository</span>
    </li>
      <li>
        <a href="/psygrammer/bayesianWork/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/psygrammer/bayesianWork/settings/collaboration" data-ga-click="Header, create new collaborator, icon:person"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/psygrammer/bayesianWork/notifications" aria-label="You have unread notifications in this repository" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
        <span class="mail-status unread"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mwU1VxOtah4hHcLUCnRTgxVhFDkNhXq2JCJUIvgTx8y9oUJ0IPH3C3Y4Qnd9JZPANmm+ZStJ1vIy5CGWIbVmYQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="jEWjW7Wmx70TGWc90wMs+fwXkm1QdQrUokt6dooBju3pjMAQluLIKm9KeYEFEf0MHED4Lp09p3gwte+ffjyt/w==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="27693910" />

      <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/psygrammer/bayesianWork/watchers">
          41
        </a>
        <a href="/psygrammer/bayesianWork/subscription"
          class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>

  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/psygrammer/bayesianWork/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="9sNXmmkgMU8MngHQzE8oKBil2wKyxDa43jH6dW2rT5uy6bnFI/zCp20TOmzVd8aXScJNCGYDsRum77WiNR0Y9Q==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar psygrammer/bayesianWork">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/psygrammer/bayesianWork/stargazers">
          4
        </a>
</form>
    <form accept-charset="UTF-8" action="/psygrammer/bayesianWork/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Euv3RtKvpFSbS3IdBag7MqcdJvFyKIoqPMPy0iqlO7hFxQDtzGplm2/qKyO+Y6uiOhz/SBBuHLMnYDQSAT/3Og==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Star this repository" title="Star psygrammer/bayesianWork">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/psygrammer/bayesianWork/stargazers">
          4
        </a>
</form>  </div>

  </li>

        <li>
          <a href="/psygrammer/bayesianWork/fork" class="minibutton with-count js-toggler-target tooltipped-n" title="Fork your own copy of psygrammer/bayesianWork to your account" aria-label="Fork your own copy of psygrammer/bayesianWork to your account" rel="facebox nofollow">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/psygrammer/bayesianWork/network" class="social-count">17</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/psygrammer" class="url fn" itemprop="url" rel="author"><span itemprop="title">psygrammer</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/psygrammer/bayesianWork" class="js-current-repository" data-pjax="#js-repo-pjax-container">bayesianWork</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/psygrammer/bayesianWork/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/psygrammer/bayesianWork" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /psygrammer/bayesianWork">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/psygrammer/bayesianWork/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /psygrammer/bayesianWork/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/psygrammer/bayesianWork/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /psygrammer/bayesianWork/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/psygrammer/bayesianWork/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /psygrammer/bayesianWork/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/psygrammer/bayesianWork/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /psygrammer/bayesianWork/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/psygrammer/bayesianWork/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /psygrammer/bayesianWork/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/psygrammer/bayesianWork/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /psygrammer/bayesianWork/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/psygrammer/bayesianWork.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:psygrammer/bayesianWork.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/psygrammer/bayesianWork" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/psygrammer/bayesianWork/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of psygrammer/bayesianWork as a zip file"
                   title="Download the contents of psygrammer/bayesianWork as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/psygrammer/bayesianWork/blob/041ce5a84fa542dd54013b1640c998ec31bcc026/djey9538/Python/python_install_guide.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:b61d097a520bb49c9ec88d860337f1af -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/psygrammer/bayesianWork/blob/joodonge/djey9538/Python/python_install_guide.md"
                 data-name="joodonge"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="joodonge">joodonge</a>
            </div>
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/psygrammer/bayesianWork/blob/master/djey9538/Python/python_install_guide.md"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/psygrammer/bayesianWork/blob/patch-1/djey9538/Python/python_install_guide.md"
                 data-name="patch-1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="patch-1">patch-1</a>
            </div>
        </div>

          <form accept-charset="UTF-8" action="/psygrammer/bayesianWork/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="0DpB9o+cU+6EpE6tJJ0umDHR63AeUMqv/0Rl7ycCuHZpidvkrDt12fdkuKOnSvc43VnKk2jS3d/JeOsROHQ0dA==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="djey9538/Python/python_install_guide.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/psygrammer/bayesianWork/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/psygrammer/bayesianWork" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">bayesianWork</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/psygrammer/bayesianWork/tree/master/djey9538" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">djey9538</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/psygrammer/bayesianWork/tree/master/djey9538/Python" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Python</span></a></span><span class="separator">/</span><strong class="final-path">python_install_guide.md</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="dongjin" class="avatar" data-user="3922468" height="24" src="https://avatars2.githubusercontent.com/u/3922468?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/djey9538" rel="contributor">djey9538</a></span>
        <time datetime="2015-02-02T16:39:15Z" is="relative-time">Feb 3, 2015</time>
        <div class="commit-title">
            <a href="/psygrammer/bayesianWork/commit/041ce5a84fa542dd54013b1640c998ec31bcc026" class="message" data-pjax="true" title="python 소개자료">python 소개자료</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="dongjin" data-user="3922468" height="24" src="https://avatars2.githubusercontent.com/u/3922468?v=3&amp;s=48" width="24" />
            <a href="/djey9538">djey9538</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>147 lines (81 sloc)</span>
          <span class="meta-divider"></span>
        <span>4.428 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/psygrammer/bayesianWork/raw/master/djey9538/Python/python_install_guide.md" class="minibutton " id="raw-url">Raw</a>
            <a href="/psygrammer/bayesianWork/blame/master/djey9538/Python/python_install_guide.md" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/psygrammer/bayesianWork/commits/master/djey9538/Python/python_install_guide.md" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->


              <a class="octicon-button js-update-url-with-hash"
                 href="/psygrammer/bayesianWork/edit/master/djey9538/Python/python_install_guide.md"
                 aria-label="Edit this file"
                 data-method="post" rel="nofollow" data-hotkey="e"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger"
               href="/psygrammer/bayesianWork/delete/master/djey9538/Python/python_install_guide.md"
               aria-label="Delete this file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h2>
<a id="user-content-파이썬-설치-가이드" class="anchor" href="#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%84%A4%EC%B9%98-%EA%B0%80%EC%9D%B4%EB%93%9C" aria-hidden="true"><span class="octicon octicon-link"></span></a>파이썬 설치 가이드</h2>

<hr>

<p>설치 관련 사이트 소개</p>

<p><a href="https://www.python.org/downloads/">파이썬 공식 다운로드</a></p>

<p><a href="https://docs.python.org/2.7//installing/index.html">파이썬 모듈 설치 Doc</a></p>

<hr>

<p>바이오 스핀 과거 자료 </p>

<p><a href="http://nbviewer.ipython.org/gist/irobii/014b8aa3574090a0d04a">ipython 설치 + 소개</a></p>

<p><a href="http://nbviewer.ipython.org/github/lexifdev/uds_study_7th/blob/master/src/__setup.ipynb">ipython + notebook 설치 가이드</a></p>

<hr>

<h1>
<a id="user-content-1-파이썬-설치" class="anchor" href="#1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%84%A4%EC%B9%98" aria-hidden="true"><span class="octicon octicon-link"></span></a>1. 파이썬 설치</h1>

<h3>
<a id="user-content-11-우분투-설치" class="anchor" href="#11-%EC%9A%B0%EB%B6%84%ED%88%AC-%EC%84%A4%EC%B9%98" aria-hidden="true"><span class="octicon octicon-link"></span></a>1.1 우분투 설치</h3>

<p>리눅스에는 기본적으로 파이썬이 설치되어 있음.</p>

<p><strong>파이썬 모듈 관리 프로그램 pip 깔기</strong> (파이썬 버전 2.7.9 부터는 이미 설치되어 있다.)</p>

<pre><code>&gt; sudo apt-get install python-pip
</code></pre>

<p><strong>파이썬 가상환경 프로그램 깔기</strong></p>

<p>(의존성 라이브러리를 독립적인 공간에 설치해준다. 필수는 아니지만, 추천사항)</p>

<pre><code>&gt; sudo pip install virtualenv
</code></pre>

<p><strong>'myenv' 라는 이름의 가상환경 사용</strong></p>

<pre><code># 가상환경 만들기
&gt; virtualenv myenv

# 가상환경 들어가기
&gt; source myenv/bin/activate

# 원하는 모듈 설치 및 작업
# 해당 모듈은 myenv 안에만 설치된다.
# 만약 가상환경 내부가 아니라면, 전역에 설치되는 것이라 sudo pip install 로 설치해야 한다.
(myenv)&gt; pip install ...

# 가상환경 끝내기
(myenv)&gt; deactivate
&gt;
</code></pre>

<p>(추가 사항)</p>

<p><a href="http://virtualenvwrapper.readthedocs.org/en/latest/install.html">virtualenvwrapper</a> 라는 프로그램은 virtualenv 여러개를 편하게 활성화 시키고 관리할 수 있게 해준다.</p>

<p>설치가 약간 복잡하다. 관심있으면 위 가이드대로 천천히 실행하면 됨.</p>

<p><br></p>

<h3>
<a id="user-content-12-윈도우-설치" class="anchor" href="#12-%EC%9C%88%EB%8F%84%EC%9A%B0-%EC%84%A4%EC%B9%98" aria-hidden="true"><span class="octicon octicon-link"></span></a>1.2 윈도우 설치</h3>

<p><strong>파이썬 설치</strong></p>

<p><a href="https://www.python.org/downloads/">다운로드 https://www.python.org/downloads/</a> 사이트에서 받아서 설치 (현재 최신버전 2.7.9)</p>

<p>그런데 설치해도, 아직 cmd 창에서 python 입력해도 실행이 안된다.</p>

<p>아직 path 추가가 안됬기 때문.</p>

<p>(Path 에 추가해야만 운영체제가 해당 프로그램을 찾을 수 있다.)</p>

<p><br></p>

<p><strong>파이썬 Path 추가</strong></p>

<p>내컴퓨터 -&gt; 속성 -&gt; 고급시스템 설정 -&gt; 환경변수</p>

<p>방법1. 시스템 변수 탭(모든 사용자에게 영향)에서 Path 값에 ;C:\Python27 추가</p>

<p>방법2. 사용자 변수 탭에서 Path 값에 (없으면 만들어서) ;C:\Python27 추가</p>

<p>(개인적으로 방법2 추천)</p>

<p>이제 cmd 창에서 python 입력하면 실행되는 것을 확인할 수 있음</p>

<p>(환경변수 등을 변경했을시에는, 새 cmd 창을 띄워야 적용된다.)</p>

<p><br></p>

<p><strong>pip 설치</strong></p>

<p>2.7.9 버전 이후부터는 이미 파이썬에 같이 들어가있다. </p>

<p>확인하고 싶으면, cmd 창에서 python -m pip freeze 라고 쳐보면 된다.</p>

<p><a href="https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py">get-pip.py</a> 파일을 다운받아, 이 파일이 있는 디렉토리 cmd 창에서 아래처럼 치면된다.</p>

<pre><code>&gt; python get-pip.py
</code></pre>

<p><strong>virtualenv 설치</strong></p>

<pre><code>&gt; python -m pip install virtualenv
</code></pre>

<p><strong>'myenv' 라는 가상환경 다루기</strong></p>

<pre><code># 가상환경 생성
&gt; python -m virtualenv myenv

# 가상환경 활성화
&gt; cd myenv/Scripts
&gt; activate
(myenv)&gt;

# 다른 모듈 설치 및 작업
(myenv)&gt; pip install ...

# 가상환경 끄기
(myenv)&gt; deactivate
&gt;
</code></pre>

<h1>
<a id="user-content-2-ipython--notebook-설치" class="anchor" href="#2-ipython--notebook-%EC%84%A4%EC%B9%98" aria-hidden="true"><span class="octicon octicon-link"></span></a>2. ipython + notebook 설치</h1>

<p><strong>ipython 설치</strong></p>

<pre><code>&gt; pip install ipython
</code></pre>

<p>(우분투의 경우, pyzmq 설치에서 에러가 발생하는데, stackoverflow 에 나온 해결 방법)</p>

<pre><code>&gt; sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
</code></pre>

<p><strong>notebook 실행에 필요한 모듈들 설치</strong></p>

<p>(<a href="https://blog.ansuchan.com/documentation-with-ipython-notebook/">ipython notebook 소개 블로그</a> 참고하였음)</p>

<pre><code>&gt; pip install jinja2 sphinx pyzmq pygments tornado nose readline  
</code></pre>

<p><strong>notebook 실행</strong></p>

<pre><code># (--pylab inline 이라는 인자를 주어야 브러우저 내에서 그래프가 그려진다.)
&gt; ipython notebook --pylab inline
</code></pre>

<p>그러면, notebook 서버가 실행되고, 브라우저로 창이 뜬다.</p>

<p>브러우저 창에서 python_beginner.ipynb 파일을 열면, 파이썬 기초 설명 내용이 나온다.</p>
</article>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.04512s from github-fe124-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-996268c2962f947579cb9ec2908bd576591bc94b6a2db184a78e78815022ba2c.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-992a73d7db34e9e3b9145958689368031792b800553bd00472f21ec8bed6fb3a.js"></script>
      
      

  </body>
</html>

