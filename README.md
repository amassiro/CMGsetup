# CMGsetup

Instructions here:

    https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMGToolsReleasesExperimental
    
Where:

    /afs/cern.ch/user/a/amassiro/work/CMG/CMSSW_9_4_6_patch1/src
    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/CMSSW_9_4_6_patch1/src
    
    
Disappearing tracks:

    https://github.com/cmg-xtracks


    
    
    
    
    
    
You start by setting up the CMGTools area following the instructions on this twiki :

    https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMGToolsReleasesExperimental#CMGTools_lite_development_releas

    cmsrel CMSSW_9_4_6_patch1
    cd CMSSW_9_4_6_patch1/src 
    cmsenv
    git cms-init

    git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_94X_dev

    cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_94X_heppy .git/info/sparse-checkout

    git checkout -b heppy_94X_dev cmg-central/heppy_94X_dev

    YOUR_GITHUB_REPOSITORY=$(git config user.github)
    git remote add origin git@github.com:$YOUR_GITHUB_REPOSITORY/cmg-cmssw.git
    git push -u origin heppy_94X_dev


    git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 94X_dev CMGTools

    cd CMGTools 

    git remote add origin  git@github.com:$YOUR_GITHUB_REPOSITORY/cmgtools-lite.git 
    git push -u origin 94X_dev
    
Then get the latest and greatest code for our analysis from our git repo

    git pull https://github.com/cmg-xtracks/cmgtools-lite.git  94X_dev

    
If needed to run on MiniAODv1 files: fix the dedx <--> track association

    git cms-addpkg DataFormats/Common
    git cms-addpkg DataFormats/TrackReco
    patch -p1 < /afs/cern.ch/user/g/gpetrucc/public/Association_fixOffsets.patch

Compile:

    cd $CMSSW_BASE/src && scram b -j 8

Then to run some tests you can go to : 

    cd CMGTools/TTHAnalysis/cfg/

Our config file is called : run_susyDeDx_cfg.py

You can run the following

    voms-proxy-init -voms cms -rfc
    
    heppy Test run_susyDeDx_cfg.py --option region=sr --option run=sig

This will produce the ntuples in the folder called Test.



