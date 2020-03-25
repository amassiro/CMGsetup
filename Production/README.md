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
      --filein file:chargino500GeV_ctau10cm_GEN-SIM-RAW_MY.root \
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

      
      
      