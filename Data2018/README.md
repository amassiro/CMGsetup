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
    
    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src    --> ok
    /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg
    
    
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

    
 
 
 
Port 10_4_X into xtrack (to be done only if new branch to commit): 
====

    where: /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/ForMigration/CMSSW_10_4_0/src/
    
 
    git clone git@github.com:cmg-xtracks/cmgtools-lite.git
    
    cd cmgtools-lite/
    
    git remote add central-cmg-amassiro git@github.com:CERN-PH-CMG/cmgtools-lite.git
    
    git fetch central-cmg-amassiro
    
    
    
    git checkout central-cmg-amassiro/104X_dev
    
    git checkout -b 104X_dev
    
    
    git push -u origin 104X_dev
    
    

    NB:
    pull = fetch + merge on current branch
    
    
 
 
New branch
====


    git checkout -b  AM_new_branch_for_2018
    
    git push -u origin AM_new_branch_for_2018
     

2018 data and MC
====

    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1D
    
    
    
    voms-proxy-init -voms cms
    xrdcp root://xrootd.unl.edu///store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/FB3B40F9-0C73-C144-BB08-8E2DFB7AD448.root  /tmp/amassiro/FB3B40F9-0C73-C144-BB08-8E2DFB7AD448.root
    
    heppy Test run_susyDeDx_2018_cfg.py --option region=cr1l   --option test=1E
    
    
    
    
Control region:
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/DATA-CR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/1May2019/DATA-CR-2018/   --option region=cr1l --option run=data   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B

    
    ls /eos/cms/store/group/phys_exotica/xtracks/1May2019/DATA-CR-2018/
    
    mkdir /tmp/test/
    cd /tmp/test/
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/DATA-CR-2018/ .
    cd DATA-CR-2018/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py DATA-CR-2018/


    mkdir /eos/cms/store/group/phys_exotica/xtracks/1May2019/DATA-CR-2018-Hadded/
    
    
     
    
    
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/MC-CR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/1May2019/MC-CR-2018/   --option region=cr1l --option run=mc   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B

                                                 
    ls /eos/cms/store/group/phys_exotica/xtracks/1May2019/MC-CR-2018/
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/MC-CR-2018/ .
    cd MC-CR-2018/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py MC-CR-2018/

    mkdir /eos/cms/store/group/phys_exotica/xtracks/1May2019/MC-CR-2018-Hadded/
    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/MC-CR-2018/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/MC-CR-2018/ "$1" 1  "}'
    

After calibration performed:

    export X509_USER_PROXY=/afs/cern.ch/user/a/amassiro/private/cms.proxy
    
    
    voms-proxy-init -voms cms
    
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-DATA-CR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-CR-2018/   --option region=cr1l --option run=data   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B


    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-MC-CR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-CR-2018/   --option region=cr1l --option run=mc   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B

                                                 
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-DATA-SR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/   --option region=sr --option run=data   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B


    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-MC-SR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-SR-2018/   --option region=sr --option run=mc   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-MC-ext-SR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-ext-SR-2018/   --option region=sr --option run=mc   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-2018/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B


    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-new-2018/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-new-2018/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                             
                                                 
                                                 
    heppy_batch.py  run_susyDeDx_2018_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-MC-SR-2018-Apendix/\
                                                 -r    /store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-SR-2018-Apendix/   --option region=sr --option run=mc   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
    
    

     
     
    hadd tree1.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_1*.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_2*.root   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_3*.root

    
    hadd tree2.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_4*.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_5*.root 
    
    hadd tree3.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_6*.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_7*.root 
    
    hadd tree4.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_8*.root /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018/MET_Run2018D_PromptReco_v2/treeProducerXtracks_tree_9*.root 
    
    cp tree1.root  /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018-Hadded/MET_Run2018D_PromptReco_v2_1/treeProducerXtracks/tree.root
    cp tree2.root  /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018-Hadded/MET_Run2018D_PromptReco_v2_2/treeProducerXtracks/tree.root
    cp tree3.root  /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018-Hadded/MET_Run2018D_PromptReco_v2_3/treeProducerXtracks/tree.root
    cp tree4.root  /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-SR-2018-Hadded/MET_Run2018D_PromptReco_v2_4/treeProducerXtracks/tree.root
    
    
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/1May2019/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Calibrated-DATA-CR-2018/ .
    cd Calibrated-DATA-CR-2018/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-DATA-CR-2018/


    mkdir /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-DATA-CR-2018-Hadded/
                                                 
      
    ls Calibrated-SIG-SR-2018/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-2018/"$1"   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-2018-Hadded/"}'
    ls Calibrated-MC-SR-2018/ | grep -v Chunk | awk '{print "cp -r Calibrated-MC-SR-2018/"$1"   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-SR-2018-Hadded/"}'
    ls Calibrated-MC-CR-2018/ | grep -v Chunk | awk '{print "cp -r Calibrated-MC-CR-2018/"$1"   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-CR-2018-Hadded/"}'
    
    ls Calibrated-MC-SR-2018-Apendix/ | grep -v Chunk | awk '{print "cp -r Calibrated-MC-SR-2018-Apendix/"$1"   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-MC-SR-2018-Apendix-Hadded/"}'
    ls Calibrated-SIG-SR-new-2018/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-new-2018/"$1"   /eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-new-2018-Hadded/"}'

         
    ls --color=never  /tmp/test/SIG-SR/ | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/SIG-SR/ "$1" 0  "}'
    ls --color=never  /tmp/test3/Calibrated-MC-SR-2018/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test3/Calibrated-MC-SR-2018/ "$1" 0  "}'
    ls --color=never  /tmp/test/Calibrated-MC-SR-2018-Apendix/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix "$1" 0  "}'
    ls --color=never  /tmp/test2/Calibrated-SIG-SR-new-2018/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test2/Calibrated-SIG-SR-new-2018/ "$1" 0  "}'

         -->   0 for k-factor=1 , 1 for Z, 2 for W
    
    
    ls --color=never  /tmp/test3/Calibrated-MC-SR-2018-Hadded-2/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test3/Calibrated-MC-SR-2018-Hadded-2/ "$1" 0  "}'
    ls --color=never  /tmp/test/Calibrated-SIG-SR-2018-Hadded/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-2018-Hadded/ "$1" 0  "}'

    
    ls --color=never  Calibrated-MC-SR-2018/  | grep -v "Chunk" | awk '{print "rm -r Calibrated-MC-SR-2018/"$1}'
    
                                                 
NB:

    downloadTreesFromEOS.py
 
           -h, --help           show this help message and exit
           -t TREEPRODUCERNAME  Name of the tree producer module
           -T TREENAME          Name of the tree file
           -c, --continue       Continue downloading if a chunk failed and print a
                                summary at the end
           -j NJOBS             Number of parallel downloading tasks

    
Fixes:
    
    ls  --color=none DATA-CR-2018/ | awk {'print "if [ ! -f \"DATA-CR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv DATA-CR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none MC-CR-2018/ | awk {'print "if [ ! -f \"MC-CR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv MC-CR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    
    ls  --color=none Calibrated-DATA-CR-2018/ | awk {'print "if [ ! -f \"Calibrated-DATA-CR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv Calibrated-DATA-CR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-DATA-SR-2018/ | awk {'print "if [ ! -f \"Calibrated-DATA-SR-2018/"$1"/isoTrackFastSkim/events.pck\" ]; then  echo \"mv Calibrated-DATA-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-DATA-SR-2018/ | awk {'print "if [ ! -f \"Calibrated-DATA-SR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv Calibrated-DATA-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    
    ls  --color=none Calibrated-MC-SR-2018/ | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-MC-SR-2018/ | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/metAnalyzer/events.pck\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-MC-SR-2018/ | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-MC-SR-2018/ | grep -v "DYJetsToLL_M50_HT200to400_Chunk101" | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    
    ls  --color=none Calibrated-MC-SR-2018/ | grep "ZvvJets_HT400to600_Chunk" | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    
    ls  --color=none Calibrated-MC-SR-2018/ | grep "DYJetsToLL_M50_HT200to400_Chunk" | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-MC-SR-2018/ | grep "ZvvJets_HT100to200_Chunk" | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    ls  --color=none Calibrated-MC-SR-2018/ | grep "QCD_HT300to500_Chunk" | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018/"$1"/JSONAnalyzer/RLTInfo.root\" ]; then  echo \"mv Calibrated-MC-SR-2018/"$1" .\"; fi"'}  | /bin/sh
    
    
    
    ls  --color=none Calibrated-MC-SR-2018-Apendix/ | awk {'print "if [ ! -f \"Calibrated-MC-SR-2018-Apendix/"$1"/PileUpAnalyzer/puWeight.pck\" ]; then  echo \"mv Calibrated-MC-SR-2018-Apendix/"$1" .\"; fi"'}  | /bin/sh

    
    ls  --color=none Calibrated-SIG-SR-new-2018/ | awk {'print "if [ ! -f \"Calibrated-SIG-SR-new-2018/"$1"/skimAnalyzerCount/SkimReport.pck\" ]; then  echo \"mv Calibrated-SIG-SR-new-2018/"$1" .\"; fi"'}  | /bin/sh
    ls  --color=none Calibrated-SIG-SR-new-2018/ | awk {'print "if [ ! -f \"Calibrated-SIG-SR-new-2018/"$1"/leptonAnalyzer/events.pck\" ]; then  echo \"mv Calibrated-SIG-SR-new-2018/"$1" .\"; fi"'}  | /bin/sh
    ls  --color=none Calibrated-SIG-SR-new-2018/ | awk {'print "if [ ! -f \"Calibrated-SIG-SR-new-2018/"$1"/isoTrackDeDxAna/events.pck\" ]; then  echo \"mv Calibrated-SIG-SR-new-2018/"$1" .\"; fi"'}  | /bin/sh
    ls  --color=none Calibrated-SIG-SR-new-2018/ | awk {'print "if [ ! -f \"Calibrated-SIG-SR-new-2018/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-new-2018/"$1" .\"; fi"'}  | /bin/sh





        
        
    
    
Summary of failed download attempts (7 in total):
Chunk ./amassiro.cc does not contain url file ./amassiro.cc/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018B_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018B_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018A_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018A_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018C_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018C_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./SingleMuon_Run2018B_17Sep2018_Chunk130 does not contain url file ./SingleMuon_Run2018B_17Sep2018_Chunk130/treeProducerXtracks/tree.root.url
Chunk ./SingleMuon_Run2018D_PromptReco_v2_Chunk193 does not contain url file ./SingleMuon_Run2018D_PromptReco_v2_Chunk193/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018D_PromptReco_v2.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018D_PromptReco_v2.cfg/treeProducerXtracks/tree.root.url



Summary of failed download attempts (8 in total):
Chunk ./jobs_desc_DYJetsToLL_M50_HT400to600.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT400to600.cfg/treeProducerXtracks/tree.root.url
Chunk ./amassiro.cc does not contain url file ./amassiro.cc/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_DYJetsToLL_M50_HT200to400.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT200to400.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_DYJetsToLL_M50_HT100to200.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT100to200.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_DYJetsToLL_M50_HT800to1200.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT800to1200.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_DYJetsToLL_M50_HT400to600_ext2.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT400to600_ext2.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_DYJetsToLL_M50_HT600to800.cfg does not contain url file ./jobs_desc_DYJetsToLL_M50_HT600to800.cfg/treeProducerXtracks/tree.root.url
Chunk ./DYJetsToLL_M50_HT100to200_Chunk36 does not contain url file ./DYJetsToLL_M50_HT100to200_Chunk36/treeProducerXtracks/tree.root.url


Missing:

    DY: 100to200, 1200to2500, 2500toInf
    WJets: 2500toInf
    ZvvJets: 200to400, 2500toInf
    
    QCD_HT100to200
    QCD_HT500to700
    DYJetsToLL_M50_HT600to800
    WJetsToLNu_HT1200to2500
    
--> -Appendix



python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ DYJetsToLL_M50_HT100to200 1  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ DYJetsToLL_M50_HT1200to2500 1  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ DYJetsToLL_M50_HT2500toInf 1  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ DYJetsToLL_M50_HT600to800 1  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ QCD_HT100to200 0  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ QCD_HT500to700 0  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ WJetsToLNu_HT1200to2500 2  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ WJetsToLNu_HT2500toInf 2  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ ZvvJets_HT200to400 1  
python addSumWgt.py /tmp/test/Calibrated-MC-SR-2018-Apendix/ ZvvJets_HT2500toInf 1  





ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/DYJetsToLL_M50_HT100to200
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/QCD_HT100to200
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/ZvvJets_HT200to400
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/DYJetsToLL_M50_HT1200to2500
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/QCD_HT500to700
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/ZvvJets_HT2500toInf
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/DYJetsToLL_M50_HT2500toInf
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/WJetsToLNu_HT1200to2500
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/DYJetsToLL_M50_HT600to800
ln -s ../Calibrated-MC-SR-2018-Apendix-Hadded/WJetsToLNu_HT2500toInf
