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
    
If in the last instruction you get errors because of " the remote contains work that you do not have locally", try first "pull":

    git pull origin 94X_dev
    
    
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
    heppy Test run_susyDeDx_cfg.py --option region=sr   --option test=1S
    heppy Test run_susyDeDx_cfg.py --option region=sr   --option test=1A
    heppy Test run_susyDeDx_cfg.py --option region=sr   --option test=1D
 
 
    
This will produce the ntuples in the folder called Test.


Copy file from grid
====

Example:
 
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/MET/MINIAOD/PromptReco-v1/000/302/526/00000/A614054F-3E97-E711-B972-02163E019B58.root test.root    --> miniaodv1, not good
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/DoubleEG/MINIAOD/17Nov2017-v1/30000/ACC2A6E6-FCD6-E711-B0E2-0242AC1C0500.root      ---> miniaodv2, good but not working
    
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/DoubleEG/MINIAOD/31Mar2018-v1/00000/C0914411-F636-E811-8796-44A84225D36F.root  --> good version
 

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
    
    
    
    
    
    voms-proxy-init -voms cms -rfc
    
    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCH/  --option region=cr1l --option run=data   \
             -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    heppy_batch.py  run_susyDeDx_cfg.py       -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MYBATCH2/  --option region=cr1l --option run=data   \
             -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    

    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-SR/\
    -r    /store/cmst3/user/amassiro/CMG/Data-SR/    --option region=sr --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L/\
    -r    /store/cmst3/user/amassiro/CMG/Data-CR1L/    --option region=cr1l --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR/\
    -r    /store/cmst3/user/amassiro/CMG/MC-SR/    --option region=sr --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L/\
    -r    /store/cmst3/user/amassiro/CMG/MC-CR1L/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/SIG-SR/\
    -r    /store/cmst3/user/amassiro/CMG/SIG-SR/    --option region=sr --option run=sig   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    
    
    
    
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-NewGeometry/\
    -r    /store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-NewGeometry/\
    -r    /store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry/    --option region=cr1l --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    
    
    
    condor_q -af HoldReason
    
    
    eoscms quota /eos/cms/store/cmst3/user/amassiro/CMG/
    
    mv /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/    /eos/cms/store/user/amassiro/CMG/disappearing/
    mv /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L/    /eos/cms/store/user/amassiro/CMG/disappearing/
    
    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/Data-SR/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/Data-SR/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/Data-SR/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/SIG-SR/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/SIG-SR/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/SIG-SR/"$1"/tree*.root"}'

    
    
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

This last part will download needed packages like:

    EgammaAnalysis  PhysicsTools  RecoEgamma  RecoTauTag
    
    
Near the bottom of the pull request, in the merge box, click command line instructions. Follow the sequence of steps to bring down the proposed pull request.

    git clone https://github.com/gpetruc/cmgtools-lite.git    CMGTools
    
    git fetch origin  pull/18/head:cmg-xtracks:trackerTopology_and_AOD


Checkout a pull request, change and prepare a new pull request
====

See comment:

    Add more commits by pushing to the trackerTopology_and_AOD branch on gpetruc/cmgtools-lite.

Run:

    git clone https://github.com/gpetruc/cmgtools-lite.git    CMGTools
    
    git checkout   trackerTopology_and_AOD

    git remote rm origin
    
    git remote add origin git@github.com:amassiro/cmgtools-lite.git
    
    git fetch origin
    
    git push -u origin trackerTopology_and_AOD
    
       ---> "-u" to track commits
       
Now I have here the branch needed: https://github.com/amassiro/cmgtools-lite

E.g.: /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/python





       
    
    




    
    
    