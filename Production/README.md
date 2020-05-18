Production of private sample
====

Where:

    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/Production/CMSSW_9_4_7/src
    
Input: 
    
    /store/group/phys_susy/xtracks/500GeV10cm_noFilter/


    /eos/cms/store/group/phys_susy/xtracks/500GeV10cm/GEN-SIM/    
    
    /eos/cms/store/group/phys_susy/xtracks/500GeV10cm/GEN-SIM/chargino500GeV_ctau10cm_GEN-SIM_144.root

    
    
# SIM-DIGI step with PU premixing

From

    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/Production/CMSSW_9_4_7/src
    
    
    
    
        cmsDriver.py \
        --datatier GEN-SIM-RAW \
        --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" \
        --conditions 94X_mc2017_realistic_v11 \
        --mc \
        --eventcontent PREMIXRAW \
        --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT \
        --nThreads 8 \
        --datamix PreMix \
        --era Run2_2017 \
        --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM_${iJob}.root \
        --fileout file:chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.root \
        --python_filename scripts/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.py \
        --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
        --customise_commands 'process.PREMIXRAWEventContent.outputCommands.extend(["keep *_trackingParticleRecoTrackAsssociation_*_*", "keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*"])' \
        -n -1751 \
        --no_exec



        cmsDriver.py \
        --datatier GEN-SIM-RAW \
        --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" \
        --conditions 94X_mc2017_realistic_v11 \
        --mc \
        --eventcontent PREMIXRAW \
        --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT \
        --nThreads 8 \
        --datamix PreMix \
        --era Run2_2017 \
        --filein file:/eos/cms/store/group/phys_susy/xtracks/500GeV10cm/GEN-SIM/chargino500GeV_ctau10cm_GEN-SIM_144.root \
        --fileout file:chargino500GeV_ctau10cm_GEN-SIM-RAW_MY.root \
        --python_filename chargino500GeV_ctau10cm_GEN-SIM-RAW_MY.py \
        --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
        --customise_commands 'process.PREMIXRAWEventContent.outputCommands.extend(["keep *_trackingParticleRecoTrackAsssociation_*_*", "keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*"])' \
        -n -1751 \
        --no_exec


Output in :

        /eos/cms/store/cmst3/user/amassiro/CMG/chargino500GeV_ctau10cm_GEN-SIM-RAW_MY.root

        
GENSIM:   93X_mc2017_realistic_v3
94X_mc2017_realistic_v11
        
        
        
# RECO step


From

    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/Production/CMSSW_9_4_7/src
    
    
      cmsDriver.py \
      --step RAW2DIGI,RECO,RECOSIM,EI \
      --mc \
      --datatier RECO \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent AODSIM \
      --era Run2_2017 \
      --nThreads 8 \
      --runUnscheduled  \
      --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.root \
      --fileout file:chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.root \
      --python_filename scripts/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.AODSIMEventContent.outputCommands.extend(["keep *_siPixelClusters_*_*", "keep *_siStripClusters_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*"])' \
      -n -1 \
      --no_exec

      
      
      
      cmsDriver.py \
      --step RAW2DIGI,RECO,RECOSIM,EI \
      --mc \
      --datatier RECO \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent AODSIM \
      --era Run2_2017 \
      --nThreads 8 \
      --runUnscheduled  \
      --filein file:/tmp/amassiro/chargino500GeV_ctau10cm_GEN-SIM-RAW_MY.root \
      --fileout file:/tmp/amassiro/chargino500GeV_ctau10cm_GEN-SIM-RAW-RECO_MY.root \
      --python_filename chargino500GeV_ctau10cm_GEN-SIM-RAW-RECO_MY.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.AODSIMEventContent.outputCommands.extend(["keep *_siPixelClusters_*_*", "keep *_siStripClusters_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "keep *_trackingParticleRecoTrackAsssociation_*_*"])' \
      -n -1 \
      --no_exec

      
      
      
      
# MINIAOD step

      cmsDriver.py miniAOD \
      --step PAT \
      --datatier MINIAODSIM \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent MINIAODSIM \
      --era Run2_2017 \
      --mc \
      --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.root \
      --fileout file:chargino${mass}GeV_ctau${length}cm_miniAOD_${iJob}.root \
      --python_filename scripts/chargino${mass}GeV_ctau${length}cm_miniAOD_${iJob}.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.MINIAODSIMEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*"])' \
      -n -1 \
      --no_exec \
      --runUnscheduled

      
      
      
      cmsDriver.py miniAOD \
      --step PAT \
      --datatier MINIAODSIM \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent MINIAODSIM \
      --era Run2_2017 \
      --mc \
      --filein file:/tmp/amassiro/chargino500GeV_ctau10cm_GEN-SIM-RAW-RECO_MY.root \
      --fileout file:/tmp/amassiro/chargino500GeV_ctau10cm_miniaod_MY.root \
      --python_filename chargino500GeV_ctau10cm_miniAOD_MY.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.MINIAODSIMEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*"])' \
      -n -1 \
      --no_exec \
      --runUnscheduled



      
      
      

 
    
New signal samples, without MET cut at gen level
====

    supernew
    
    #/eos/cms/store/group/phys_susy/xtracks/500GeV10cm_noFilter/miniAOD
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    cmsenv
    
    voms-proxy-init -voms cms -rfc
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/ .
    cd Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/


    ls  --color=never   Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-supernew-nometfilter-myGT-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-supernew-nometfilter-myGT-2017-Hadded/"}'

    
    
    
    

 
    
New signal samples by Filip with GT 2017
====

    supernew
    
    /eos/cms/store/group/phys_susy/xtracks/500GeV10cm_GTv11/miniAOD
    /eos/cms/store/group/phys_susy/xtracks/600GeV10cm_GTv11/miniAOD
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    cmsenv
    
    voms-proxy-init -voms cms -rfc
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-newGT-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-newGT-2017/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-newGT-2017/ .
    cd Calibrated-SIG-SR-newGT-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-newGT-2017/


    ls  --color=never   Calibrated-SIG-SR-newGT-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-newGT-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-newGT-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/Calibrated-SIG-SR-newGT-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-newGT-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-newGT-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-newGT-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-newGT-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-newGT-2017-Hadded/"}'

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    correct and with met cut, 2017
    
         M=300, 1cm production (with MET filter at 150 GeV):
         /eos/cms/store/group/phys_susy/xtracks/300GeV1cm_2017/miniAOD
         
         M=300, 30cm production (with MET filter at 150 GeV):
         /eos/cms/store/group/phys_susy/xtracks/300GeV30cm_2017/miniAOD
         
         M=900, 1cm production (with MET filter at 150 GeV):
         /eos/cms/store/group/phys_susy/xtracks/900GeV1cm_2017/miniAOD
         
         M=900, 30 cm production (with MET filter at 150 GeV):
         /eos/cms/store/group/phys_susy/xtracks/900GeV30cm_2017/miniAOD
         
         M=500, 1cm production (with MET filter at 150 GeV):
         /eos/cms/store/group/phys_susy/xtracks/500GeV1cm_2017/miniAOD
         
         And, for completeness, this one which we already had previously:
         M=500, 10cm production (with MET filter at 150 GeV)
         /eos/cms/store/group/phys_susy/xtracks/500GeV10cm_newGT/miniAOD
    
    
    cd /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/
    
    cmsenv
    
    voms-proxy-init -voms cms -rfc
    
    
    
    
    heppy_batch.py  run_susyDeDx_cfg.py     -o  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-metfilter-newGT-2017/\
                                                 -r    /store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017-18thMay/   --option region=sr --option run=sig   \
                                                 -b 'run_condor_simple.sh -t 480 ./batchScript.sh' -B
                                                 
                                                 
    mkdir /tmp/test/
    cd /tmp/test/
    
    cp -r /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/cfg/Calibrated-SIG-SR-metfilter-newGT-2017/ .
    cd Calibrated-SIG-SR-metfilter-newGT-2017/

    downloadTreesFromEOS.py -t treeProducerXtracks  .   -c    -j 4
    
    cd ../
    
    haddChunks.py Calibrated-SIG-SR-metfilter-newGT-2017/


    ls  --color=never   Calibrated-SIG-SR-metfilter-newGT-2017/  | awk {'print "if [ ! -f \"Calibrated-SIG-SR-metfilter-newGT-2017/"$1"/JSONAnalyzer/JSON.pck\" ]; then  echo \"mv Calibrated-SIG-SR-metfilter-newGT-2017/"$1" .\"; fi"'}  | /bin/sh

    
    cd  /afs/cern.ch/work/a/amassiro/CMG/DisappearingTracks/6Mar2019/CMSSW_9_4_6_patch1/src/CMGTools/TTHAnalysis/macros/xtracks/
    ls --color=never  /tmp/test/Calibrated-SIG-SR-metfilter-newGT-2017/  | grep -v "Chunk" | grep -v "jobs"  | awk '{print "python addSumWgt.py /tmp/test/Calibrated-SIG-SR-metfilter-newGT-2017/ "$1" 0  "}'
    

    
    mkdir /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017-Hadded/
                                                 
    ls Calibrated-SIG-SR-metfilter-newGT-2017/ | grep -v Chunk | awk '{print "cp -r Calibrated-SIG-SR-metfilter-newGT-2017/"$1"   /eos/cms/store/group/phys_exotica/xtracks/6Mar2019/Calibrated-SIG-SR-metfilter-newGT-2017-Hadded/"}'

    
    
      