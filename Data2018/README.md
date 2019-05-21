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
    
    
    
    
    
Summary of failed download attempts (7 in total):
Chunk ./amassiro.cc does not contain url file ./amassiro.cc/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018B_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018B_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018A_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018A_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018C_17Sep2018.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018C_17Sep2018.cfg/treeProducerXtracks/tree.root.url
Chunk ./SingleMuon_Run2018B_17Sep2018_Chunk130 does not contain url file ./SingleMuon_Run2018B_17Sep2018_Chunk130/treeProducerXtracks/tree.root.url
Chunk ./SingleMuon_Run2018D_PromptReco_v2_Chunk193 does not contain url file ./SingleMuon_Run2018D_PromptReco_v2_Chunk193/treeProducerXtracks/tree.root.url
Chunk ./jobs_desc_SingleMuon_Run2018D_PromptReco_v2.cfg does not contain url file ./jobs_desc_SingleMuon_Run2018D_PromptReco_v2.cfg/treeProducerXtracks/tree.root.url



 
