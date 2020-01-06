import glob
import pickle
import sys
from ROOT import *
from array import array


args = sys.argv[1:]

input_file  = args[0]
output_file = args[1]

print " input_file = ",  input_file
print " output_file = ", output_file


treefile = TFile(input_file, "read")
tree     = treefile.Get("tree")
entries  = tree.GetEntries()

print " entries = ", entries


treefileOutput = TFile(output_file, "update")
treeOut     = treefile.Get("tree").CloneTree(0)

maxjet = 10
Jet_pt_hem = array( 'f', maxjet*[ 0. ] )
treeOut.Branch( 'Jet_pt_hem', Jet_pt_hem, 'Jet_pt_hem[nJet]/F' )

met_pt_hem = array( 'f', [ 0. ] )
treeOut.Branch( 'met_pt_hem', met_pt_hem, 'met_pt_hem/F' )



num = 0
for entry in tree :
  
  # met -> met_hem
  # Jet_pt[nJet] -> Jet_pt_hem[nJet]
  
  #print " num = ", num
  #print "   nJet = ", entry.nJet

  correction_vector = TLorentzVector(0, 0, 0, 0)

  nJet = min(entry.nJet,maxjet)
  for j in range(nJet):
    correction = 1.
    #
    # In MC, scale down the jet energy by
    # 20 % for jets with -1.57 <phi< -0.87 and -2.5<eta<-1.3
    # 35 % for jets with -1.57 <phi< -0.87 and -3.0<eta<-2.5
    #

    if entry.Jet_phi[j] > -1.57 and entry.Jet_phi[j] < -0.87 and  entry.Jet_eta[j] > -2.5 and entry.Jet_eta[j] < -1.3 and entry.Jet_pt[j]>15 : 
      correction = 0.80

    if entry.Jet_phi[j] > -1.57 and entry.Jet_phi[j] < -0.87 and  entry.Jet_eta[j] > -3.0 and entry.Jet_eta[j] < -2.5 and entry.Jet_pt[j]>15 : 
      correction = 0.65
      
    Jet_pt_hem[j] = entry.Jet_pt[j] * correction

    if correction != 1 :
      temp_correction_vector = TLorentzVector(0, 0, 0, 0)
      temp_correction_vector.SetPtEtaPhiE(Jet_pt_hem[j] - entry.Jet_pt[j] , 0 , entry.Jet_phi[j] , 0);  
      correction_vector += temp_correction_vector
    
  
  
  old_met = TLorentzVector(0, 0, 0, 0)
  old_met.SetPtEtaPhiE(entry.met_pt , 0 , entry.met_phi , 0);  

  new_met = old_met + correction_vector
  
  met_pt_hem[0] = new_met.Pt()
  
  
  # treeOut
  
  
  treeOut.Fill()
  
  num += 1
  

treeOut.AutoSave()
treefileOutput.Close()




#bwgtsumexists = False
#bkfactexists  = False
#for branch in tree.GetListOfBranches():
    #if( branch.GetName() == "wgtsum" ) :
        #bwgtsumexists = True
        #print "Branch wgtsum already exists, will not do anything to it"
    #if( branch.GetName() == "kfact" ) :
        #bkfactexists = True
        #print "Branch kfact already exists, will not do anything to it"

#bwgtsum = None
#bkfact  = None
#if not bwgtsumexists :
    #bwgtsum = tree.Branch('wgtsum', wgtsum, 'wgtsum/F')
#if not bkfactexists :
    #bkfact  = tree.Branch('kfact' , kfact , 'kfact/F')

#counter = 0
#for entry in tree :
    #if (counter % 10000 == 0) :
        #print "Processing event : " + str(counter+1)

    #kfact[0] = 1.0
    #if kid != 0 :
        #vpt = entry.lheVpt
        #if vpt > 0. and vpt < 150.1 :
            #vpt = 150.1
        #if vpt > 1199.9 :
            #vpt = 1199.9

        #if vpt > 0. and kid == 1 :
            #kfact[0] = zkfact.GetBinContent(zkfact.FindBin(vpt));
        #if vpt > 0. and kid == 2 :  
            #kfact[0] = wkfact.GetBinContent(wkfact.FindBin(vpt));

    #if not bwgtsum == None :
        #bwgtsum.Fill()
    #if not bkfact == None :
        #bkfact .Fill()
    #counter = counter+1

#print "Total events processed : " + str(counter)

