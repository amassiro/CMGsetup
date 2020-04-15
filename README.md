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
    
    heppy Test run_susyDeDx_cfg.py --option region=cr1l   --option test=1E
 
 
    
This will produce the ntuples in the folder called Test.


Copy file from grid
====

Example:
 
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/MET/MINIAOD/PromptReco-v1/000/302/526/00000/A614054F-3E97-E711-B972-02163E019B58.root test.root    --> miniaodv1, not good
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/DoubleEG/MINIAOD/17Nov2017-v1/30000/ACC2A6E6-FCD6-E711-B0E2-0242AC1C0500.root      ---> miniaodv2, good but not working
    
    xrdcp root://xrootd.unl.edu///store/data/Run2017D/DoubleEG/MINIAOD/31Mar2018-v1/00000/C0914411-F636-E811-8796-44A84225D36F.root  --> good version
 
    xrdcp root://xrootd.unl.edu///store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/FB3B40F9-0C73-C144-BB08-8E2DFB7AD448.root  --> good version for new   --> 1E
 
 
 
 
 

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
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-Test2018MC/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/MC-CR1L-Test2018MC/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/MC-SR/   --option region=sr --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-2/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/MC-SR-2/   --option region=sr --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-3/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/MC-SR-3/   --option region=sr --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-4/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/MC-SR-4/   --option region=sr --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    

    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/SIG-SR/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/SIG-SR/   --option region=sr --option run=sig   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    

    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/DATA-SR/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/DATA-SR/   --option region=sr --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/DATA-SR-2017/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/DATA-SR-2017/   --option region=sr --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    ls --color=never /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/DATA-SR-2017/ | awk '{print "hadd /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/DATA-SR-2017/tree_"$1".root   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/DATA-SR-2017/"$1"/tree*.root"}'

    
    
    

    mkdir /tmp/test/
    cd /tmp/test/
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR/ .
    cd MC-SR

    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-2/ .
    cd MC-SR-2

    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-3/ .
    cd MC-SR-3

    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-SR-4/ .
    cd MC-SR-4

    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/SIG-SR/ .
    cd SIG-SR

    downloadTreesFromEOS.py -t treeProducerXtracks  .

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c
    
    
    cd ../
    
    haddChunks.py SIG-SR/

    haddChunks.py MC-SR/

    haddChunks.py MC-SR-2/

    haddChunks.py MC-SR-3/

    haddChunks.py MC-SR-4/

     
    
Nice cleaning:

    ls  MC-SR-2/ | grep TTSemi_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep QCD_HT700to1000_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep TBar_tch_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep WJets_HT600to800_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep ZvvJets_HT600to800_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep WJets_HT100to200_Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    ls  MC-SR-2/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-2/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-2/"$1" .\"; fi"'}  | /bin/sh
    
    ls  MC-SR-3/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-3/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-3/"$1" .\"; fi"'}  | /bin/sh
    ls --color=none  MC-SR-3/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-3/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-3/"$1" .\"; fi"'}  | /bin/sh > doit.sh

    ls --color=none  MC-SR-3/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-3/"$1"/treeProducerXtracks/tree.root\" ]; then  echo \"mv MC-SR-3/"$1" .\"; fi"'}  | /bin/sh > doit.sh

    
    ls --color=none  MC-SR-4/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-4/"$1"/treeProducerXtracks/tree.root\" ]; then  echo \"mv MC-SR-4/"$1" .\"; fi"'}  | /bin/sh > doit.sh
    ls --color=none  MC-SR-4/ | grep Chunk | awk {'print "if [ ! -f \"MC-SR-4/"$1"/tauAnalyzer/events.pck\" ]; then  echo \"mv MC-SR-3/"$1" .\"; fi"'}  | /bin/sh > doit.sh

    
    
        
and now copy back on eos:


    /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/
    
    ls SIG-SR/ | grep -v "Chunk" | awk '{print "cp -r SIG-SR/"$1" /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/"}'
    ls MC-SR/  | grep -v "Chunk" | awk '{print "cp -r MC-SR/"$1" /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/"}'
    ls MC-SR-2/  | grep -v "Chunk" | awk '{print "cp -r MC-SR-2/"$1" /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/"}'
    ls MC-SR-3/  | grep -v "Chunk" | awk '{print "cp -r MC-SR-3/"$1" /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/"}'
    ls MC-SR-4/  | grep -v "Chunk" | awk '{print "cp -r MC-SR-4/"$1" /eos/cms/store/group/phys_exotica/xtracks/6Mar2019-Hadded/"}'
    

but before add wgtsum:

    
    ls --color=never  /tmp/test/SIG-SR/ | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/SIG-SR/ "$1" 0  "}'
    ls --color=never  /tmp/test/MC-SR/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-SR/ "$1" 0  "}'

    ls --color=never  /tmp/test/MC-SR-2/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-SR-2/ "$1" 0  "}'
    ls --color=never  /tmp/test/MC-SR-3/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-SR-3/ "$1" 0  "}'

    ls --color=never  /tmp/test/MC-SR-4/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-SR-4/ "$1" 0  "}'
    
    
    
    
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-NewGeometry/\
    -r    /store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-NewGeometry/\
    -r    /store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry/    --option region=cr1l --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-NewGeometry-Calibrated-and-Smeared/\
    -r    /store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-NewGeometry-Calibrated-and-Smeared/\
    -r    /store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared/    --option region=cr1l --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B

    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/\
    -r    /store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/    --option region=cr1l --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/test_geometry_Giovanni/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/\
    -r    /store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/    --option region=cr1l --option run=data   \
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

    
    
    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry/"$1"/tree*.root"}'
    
    

    
    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared/"$1"/tree*.root"}'
    
    
    
    
    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/Data-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/"$1"/tree*.root"}'

    ls --color=never /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/ | awk '{print "hadd /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/tree_"$1".root   /eos/cms/store/cmst3/user/amassiro/CMG/MC-CR1L-NewGeometry-Calibrated-and-Smeared-Correct/"$1"/tree*.root"}'
    
    
    
    cd ../macros/xtracks/    
    
    ls --color=never ../../cfg/MC-SR/ | grep -v ".cfg" | grep -v ".root" | grep DY                    | awk '{print "python addSumWgt.py /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/ "$1" 2  ../../cfg/MC-SR/"}'
    ls --color=never ../../cfg/MC-SR/ | grep -v ".cfg" | grep -v ".root" | grep Zvv                   | awk '{print "python addSumWgt.py /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/ "$1" 2  ../../cfg/MC-SR/"}'
    ls --color=never ../../cfg/MC-SR/ | grep -v ".cfg" | grep -v ".root" | grep WJets                 | awk '{print "python addSumWgt.py /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/ "$1" 1  ../../cfg/MC-SR/"}'
    ls --color=never ../../cfg/MC-SR/ | grep -v ".cfg" | grep -v ".root" | grep -v WJets | grep -v DY | grep -v Zvv| awk '{print "python addSumWgt.py /eos/cms/store/cmst3/user/amassiro/CMG/MC-SR/ "$1" 0  ../../cfg/MC-SR/"}'
    
    
    ls --color=never ../../cfg/SIG-SR/ | grep -v ".cfg" | grep -v ".root"                             | awk '{print "python addSumWgt.py /eos/cms/store/cmst3/user/amassiro/CMG/SIG-SR/ "$1" 2  ../../cfg/SIG-SR/"}'
    
    
    ---> /eos/cms/store/group/phys_exotica/xtracks/
    
    ls --color=never /eos/cms/store/group/phys_exotica/xtracks/MC-SR/ | awk '{print "hadd /eos/cms/store/group/phys_exotica/xtracks/MC-SR/tree_"$1".root  /eos/cms/store/group/phys_exotica/xtracks/MC-SR/"$1"/tree*.root"}'
    ls --color=never /eos/cms/store/group/phys_exotica/xtracks/SIG-SR/ | awk '{print "hadd /eos/cms/store/group/phys_exotica/xtracks/SIG-SR/tree_"$1".root  /eos/cms/store/group/phys_exotica/xtracks/SIG-SR/"$1"/tree*.root"}'
    
    
    
    
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





       
    
    


    
New branch
====

    git checkout -b  AM_new_branch_for_2017
    
    git push -u origin AM_new_branch_for_2017
    
    

2018 data and MC
====

    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1D
    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1E
 
 
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-2018/\
    -r  /store/group/phys_exotica/xtracks/1Apr2019/DATA-2018-CR1l/     --option region=cr1l    --option run=data   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-2018/\
    -r  /store/group/phys_exotica/xtracks/1Apr2019/MC-2018-CR1l/     --option region=cr1l    --option run=mc   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    hadd      /eos/cms/store/group/phys_exotica/xtracks/1Apr2019/MC-2018-CR1l/tree_DYJetsM50_HT100to200.root   /eos/cms/store/group/phys_exotica/xtracks/1Apr2019/MC-2018-CR1l/DYJetsM50_HT100to200/tree*.root

    
    
    mkdir /tmp/test/
    cd /tmp/test/
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/MC-CR1L-2018/ .
    cd MC-CR1L-2018

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c
    
    cd ../
    haddChunks.py MC-CR1L-2018/

    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    
    ls --color=never  /tmp/test/MC-CR1L-2018/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-CR1L-2018/ "$1" 0  "}'
    
    
    ls MC-CR1L-2018/  | grep -v "Chunk" | awk '{print "cp -r MC-CR1L-2018/"$1" /eos/cms/store/group/phys_exotica/xtracks/1Apr2019-Hadded-2018/"}'

    
    
    
    
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Data-CR1L-2018/ .
    cd Data-CR1L-2018

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c
    
    cd ../
    haddChunks.py Data-CR1L-2018/
    
    ls --color=none   Data-CR1L-2018/   | grep Chunk | awk {'print "if [ ! -f \"Data-CR1L-2018/"$1"/treeProducerXtracks/tree.root\" ]; then  echo \"mv  Data-CR1L-2018/"$1" .\"; fi"'}  | /bin/sh > doit.sh
    
    
    ls Data-CR1L-2018/  | grep -v "Chunk" | awk '{print "cp -r Data-CR1L-2018/"$1" /eos/cms/store/group/phys_exotica/xtracks/1Apr2019-Hadded-2018/"}'

    
    
    
    
 
Zmumu skim 
====

|  /SingleMuon/Run2017B-ZMu-PromptReco-v1/RAW-RECO  |
|  /SingleMuon/Run2017B-ZMu-PromptReco-v2/RAW-RECO  |
|  /SingleMuon/Run2017C-ZMu-PromptReco-v1/RAW-RECO  |
|  /SingleMuon/Run2017C-ZMu-PromptReco-v2/RAW-RECO  |
|  /SingleMuon/Run2017C-ZMu-PromptReco-v3/RAW-RECO  |
|  /SingleMuon/Run2017D-ZMu-PromptReco-v1/RAW-RECO  |
|  /SingleMuon/Run2017E-ZMu-PromptReco-v1/RAW-RECO  |
|  /SingleMuon/Run2017F-ZMu-PromptReco-v1/RAW-RECO  |



Test:

    xrdcp root://xrootd.unl.edu///store/data/Run2017C/SingleMuon/RAW-RECO/ZMu-PromptReco-v3/000/300/777/00000/A0607B19-6C7E-E711-A83B-02163E0136CF.root /tmp/amassiro/test.root 
    
    
    cmsDriver.py step2 --filein file:/tmp/amassiro/test.root  --fileout file:/tmp/amassiro/test.reco.root  --data --eventcontent FEVTDEBUGHLT --runUnscheduled --datatier FEVTDEBUGHLT --conditions 94X_dataRun2_v11  --step RAW2DIGI,RECO --nThreads 8 --era Run2_2017 --python_filename reco_data_ZmumuSkim_cfg.py --no_exec -n 10

    change the name of the process from "RECO" to "MyRECO"
    
    cmsRun reco_data_ZmumuSkim_cfg.py
      

    cmsDriver.py step12 --filein file:/tmp/amassiro/test.reco.root  --fileout file:/tmp/amassiro/test.reco.aod.root  --data --eventcontent MINIAOD --runUnscheduled --datatier MINIAOD --conditions 94X_dataRun2_v11  --step PAT --nThreads 8 --era Run2_2017 --python_filename aod_data_ZmumuSkim_cfg.py   --scenario pp --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2017      --no_exec -n 10

    cmsDriver.py step12 --filein file:/tmp/amassiro/test.reco.root  --fileout file:/tmp/amassiro/test.reco.aod.root  --data --eventcontent MINIAOD --runUnscheduled --datatier MINIAOD --conditions 94X_dataRun2_v11  --step PAT --nThreads 8 --era Run2_2017 --python_filename aod_data_ZmumuSkim_cfg.py   --scenario pp       --no_exec -n 10

    
    cmsDriver.py step12 --filein file:/tmp/amassiro/test.reco.root  --fileout file:/tmp/amassiro/test.reco.aod.root  --data --eventcontent MINIAOD --runUnscheduled --datatier MINIAOD --conditions 94X_dataRun2_v11  --step PAT --nThreads 8 --era Run2_2017 --python_filename aod_data_ZmumuSkim_cfg.py   --scenario pp   --customise_commands 'process.MINIAODEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*", "keep *_siPixelClusters_*_*", "keep *_siStripClusters_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*", "drop TotemRPLocalTracked*_*_*_*", "drop CTPPSLocalTrackLites_*_*_*"])'    --no_exec -n 10

    
    
    
    
    
    cmsDriver.py step12 --filein file:/tmp/amassiro/test.reco.root  --fileout file:/tmp/amassiro/test.reco.aod.root  --data --eventcontent MINIAOD --runUnscheduled --datatier MINIAOD --conditions 94X_dataRun2_v11  --step PAT --nThreads 8 --era Run2_2017 --python_filename aod_data_ZmumuSkim_cfg.py --customise_commands 'process.MINIAODEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*", "keep *_siPixelClusters_*_*", "keep *_siStripClusters_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*"])'   --scenario pp --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2017      --no_exec -n 10
    
    change the name of the process from "RECO" to "MyRECO"
    
    edmConfigDump aod_data_ZmumuSkim_cfg.py > dump_aod_data_ZmumuSkim_cfg.py

    cmsRun aod_data_ZmumuSkim_cfg.py

    
    
 
 
    cmsDriver.py step12 --filein file:/tmp/amassiro/test.root  --fileout file:/tmp/amassiro/test.reco.aod.root  --data --eventcontent MINIAOD --runUnscheduled --datatier MINIAOD --conditions 94X_dataRun2_v11  --step RAW2DIGI,RECO,PAT --nThreads 8 --era Run2_2017 --python_filename recoaod_data_ZmumuSkim_cfg.py --customise_commands 'process.MINIAODEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*", "keep *_siPixelClusters_*_*", "keep *_siStripClusters_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*"])'         --no_exec -n 10
    
    change the name of the process from "RECO" to "MyRECO"
    
    edmConfigDump recoaod_data_ZmumuSkim_cfg.py > dump_recoaod_data_ZmumuSkim_cfg.py

    cmsRun recoaod_data_ZmumuSkim_cfg.py
    
    

    

2017 prefire test
====

Where:

    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg
    
    
Data test:

    xrdcp root://xrootd.unl.edu///store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/FB3B40F9-0C73-C144-BB08-8E2DFB7AD448.root    /tmp/amassiro/
    
    
    heppy Test run_susyDeDx_onlyPrefire_cfg.py --option region=cr1l   --option test=1E   --option run=mc
    heppy Test run_susyDeDx_onlyPrefire_cfg.py --option region=cr1l   --option test=1E   --option run=mc   -N 1000

    
Now on grid for signal samples:

    
    voms-proxy-init -voms cms -rfc
    
    export X509_USER_PROXY=$HOME/private/cms.proxy

    
    heppy_batch.py  run_susyDeDx_onlyPrefire_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/SIG-SR-PREFIRE/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/SIG-SR-PREFIRE/   --option region=sr --option run=sig   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_onlyPrefire_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/SIG-SR-PREFIRE-supernew/\
    -r    /store/group/phys_exotica/xtracks/6Mar2019/SIG-SR-PREFIRE-supernew/   --option region=sr --option run=sig   \
    -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    
    
In case of problems while submitting on condor

    export X509_USER_PROXY=$HOME/private/cms.proxy

    
    
    
    
New signal samples
====

    supernew
    
    #/eos/cms/store/group/phys_susy/xtracks/600GeV10cm/
    #/eos/cms/store/group/phys_susy/xtracks/300GeV30cm/
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-2017/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-2017/ .
    cd Calibrated-SIG-SR-supernew-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-supernew-2017/


    ls  --color=never   Calibrated-SIG-SR-supernew-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-supernew-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-supernew-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/Calibrated-SIG-SR-supernew-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-supernew-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-supernew-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-supernew-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-2017-Hadded/"}'

    


 
    
New signal samples, without MET cut at gen level
====

    supernew
    
    #/eos/cms/store/group/phys_susy/xtracks/500GeV10cm_noFilter/miniAOD
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    cmsenv
    
    voms-proxy-init -voms cms -rfc
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-nometfilter-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-2017/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-nometfilter-2017/ .
    cd Calibrated-SIG-SR-supernew-nometfilter-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-supernew-nometfilter-2017/


    ls  --color=never   Calibrated-SIG-SR-supernew-nometfilter-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-supernew-nometfilter-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-supernew-nometfilter-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/Calibrated-SIG-SR-supernew-nometfilter-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-supernew-nometfilter-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-supernew-nometfilter-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-supernew-nometfilter-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-2017-Hadded/"}'

    
    
    
 
New signal samples, with MET cut at gen level and correct GT
====

    supernew
    
    #/eos/cms/store/group/phys_susy/xtracks/500GeV10cm_newGT/miniAOD/
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    cmsenv
    
    voms-proxy-init -voms cms -rfc
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-metfilter-newGT-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test2/
    cd /tmp/test2/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-metfilter-newGT-2017/ .
    cd Calibrated-SIG-SR-metfilter-newGT-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-metfilter-newGT-2017/


    ls  --color=never   Calibrated-SIG-SR-metfilter-newGT-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-metfilter-newGT-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-metfilter-newGT-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test2/Calibrated-SIG-SR-metfilter-newGT-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test2/Calibrated-SIG-SR-metfilter-newGT-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-metfilter-newGT-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-metfilter-newGT-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017-Hadded/"}'

    
    

Condor problems
====

    cernbatchsubmit
    
    export _condor_SCHEDD_HOST="bigbird15.cern.ch"
    export _condor_CREDD_HOST="bigbird15.cern.ch"

    
    
    
    
    