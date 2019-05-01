2018 data
====

    cmssw -> 10_4_X
    
Inputs:
 
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
    
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable --> 10_2_5
    
    
Where:

    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_2_5/src
    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src
    
Install:


    git cms-init

    git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_104X_dev

    git checkout -b heppy_104X_dev cmg-central/heppy_104X_dev

    YOUR_GITHUB_REPOSITORY=$(git config user.github)
    git remote add origin git@github.com:$YOUR_GITHUB_REPOSITORY/cmg-cmssw.git
    git push -u origin heppy_94X_dev


    git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 104X_dev CMGTools

    cd CMGTools 

    git remote add origin  git@github.com:$YOUR_GITHUB_REPOSITORY/cmgtools-lite.git 
    git push -u origin 104X_dev
    
If in the last instruction you get errors because of " the remote contains work that you do not have locally", try first "pull":

    git pull origin 104X_dev
    
    
Then get the latest and greatest code for our analysis from our git repo

    git pull https://github.com/cmg-xtracks/cmgtools-lite.git  104X_dev

    
    
New branch
====


    git checkout -b  AM_new_branch_for_2017
    
    git push -u origin AM_new_branch_for_2017
     

2018 data and MC
====

    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1D
    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1E
 
