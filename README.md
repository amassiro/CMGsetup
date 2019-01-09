# CMGsetup

Instructions here:

    https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMGToolsReleasesExperimental
    
Where:

    /afs/cern.ch/user/a/amassiro/work/CMG/CMSSW_9_4_6_patch1/src
    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/CMSSW_9_4_6_patch1/src
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
    
    # fixes in run_susyDeDx_cfg.py
    
    heppy Test run_susyDeDx_cfg.py --option region=sr --option run=sig

    heppy Test run_susyDeDx_cfg.py --option region=cr1l --option run=mc

    heppy Test run_susyDeDx_cfg.py --option region=cr1l --option run=data
 
 
 
    heppy Test run_susyDeDx_cfg.py --option region=cr1l --option test=1A
 
    heppy Test run_susyDeDx_cfg.py --option region=cr1l --option test=1S
 
 
    
This will produce the ntuples in the folder called Test.





Add new variable
====

First define new variable in object:

    https://github.com/cmg-xtracks/cmgtools-lite/blob/94X_dev/TTHAnalysis/python/analyzers/isoTrackDeDxAnalyzer.py
    
Then add to the ntuple creator:

    https://github.com/cmg-xtracks/cmgtools-lite/blob/94X_dev/TTHAnalysis/python/analyzers/treeProducerXtracks.py
    
    

Create pull request
====

After I change the files

To check what is there around:
    
    cat .git/config
    git push ====> git push origin <branch where I am now>
 
Check which branch I am on

    git status
    
    -->    On branch 94X_dev

 
Commit:
 
    git commit -m "comment here" file.py


Push:

    git push origin 94X_dev
    
Go on website:

    https://github.com/amassiro/cmgtools-lite
    
    check my last commit is there
    
    click on "new pull request"
    
    In base fork (on the left): select to where I want to merge ---> cmg-xtracks/cmgtools-lite     94X_dev
    Head fork: select my repository with the branch defined above (94X_dev)
    
    -> Create pull request
    
    
    
    
    
    
    
    
    
    
    
Using batch system
====

CERN batch using condor or LSF

For condor, declaring 480 mins of job time (wall clock time)
        
    heppy_batch.py -o /path/to/dir run_susyDeDx_cfg.py   -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B --option region=cr1l --option run=data
 
    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCH/  --option region=cr1l --option run=data   \
             -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
             
    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/test_geometry/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCH/  --option region=cr1l --option run=data   \
             -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/test_geometry/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCHMC/  --option region=cr1l --option run=mc   \
             -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
to see running and pending jobs, use 

    condor_q

for LSF (using the default 8nh queue)
    
    heppy_batch.py -o /path/to/output/dir   cfg.py 

    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCH-lxbatch/  --option region=cr1l --option run=data 
           
        
    
you should also set X509_USER_PROXY to some place on AFS and make sure to have a valid grid proxy

    export X509_USER_PROXY=$HOME/private/cms.proxy

    voms-proxy-init -voms cms

from the output directory, you can check for failed jobs with

    cmgListChunksToResub  .

you can use the -d option to skip from the list the jobs that appear to still be running"

Also some more instructions here :

    https://github.com/cheidegg/cmgtools-lite/pull/11





    
    
    
    
Checkout a pull request
====
    
    e.g. 
    gpetruc:trackerTopology_and_AOD
    
    https://github.com/cmg-xtracks/cmgtools-lite/pull/18
    
    
    
Run:

    
    cd /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/test_geometry
    
    cmsrel CMSSW_9_4_6_patch1
    cd CMSSW_9_4_6_patch1/src 
    cmsenv
    git cms-init

    git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git  -f  -t heppy_94X_dev
    cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_94X_heppy .git/info/sparse-checkout
    git checkout -b heppy_94X_dev cmg-central/heppy_94X_dev

    
Near the bottom of the pull request, in the merge box, click command line instructions. Follow the sequence of steps to bring down the proposed pull request.

    git clone https://github.com/gpetruc/cmgtools-lite.git    CMGTools
    
    git fetch origin  pull/18/head:cmg-xtracks:trackerTopology_and_AOD


    
    
    