2018 data
====

    cmssw -> 10_4_X
    
Inputs:
 
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
    
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable --> 10_2_5
    
Instructions:

    https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMGToolsReleasesExperimental
    
    
Where:

    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_2_5/src
    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src
    
Install:


    export SCRAM_ARCH=slc7_amd64_gcc820

    cmsrel CMSSW_10_4_0
    cd CMSSW_10_4_0/src 
    cmsenv
    git cms-init

    # add the central cmg-cmssw repository to get the Heppy 104X_dev branch
    git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_104X_dev
    
    # configure the sparse checkout, and get the base heppy packages
    cp /afs/cern.ch/user/g/gpetrucc/public/sparse-checkout_104X_heppy .git/info/sparse-checkout
    git checkout -b heppy_104X_dev cmg-central/heppy_104X_dev
    
    # add your mirror, and push the 104X_dev branch to it
    YOUR_GITHUB_REPOSITORY=$(git config user.github) # or set it manually if this doesn't work for you
    git remote add origin git@github.com:$YOUR_GITHUB_REPOSITORY/cmg-cmssw.git
    git push -u origin heppy_104X_dev
    
    # now get the CMGTools subsystem from the cmgtools-lite repository
    git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 104X_dev CMGTools
    cd CMGTools 
    
    # add your fork, and push the 104X_dev branch to it
    git remote add origin  git@github.com:$YOUR_GITHUB_REPOSITORY/cmgtools-lite.git 
    git push -u origin 104X_dev

    
If in the last instruction you get errors because of " the remote contains work that you do not have locally", try first "pull":

    git pull origin 104X_dev
    
    
Compile

    cd $CMSSW_BASE/src && scram b -j 8
    
    
Then get the latest and greatest code for our analysis from our git repo

    git pull https://github.com/cmg-xtracks/cmgtools-lite.git  104X_dev
    git pull https://github.com/cmg-xtracks/cmgtools-lite.git  104X_dev

    
    
New branch
====


    git checkout -b  AM_new_branch_for_2017
    
    git push -u origin AM_new_branch_for_2017
     

2018 data and MC
====

    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1D
    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1E
 
