
from multiprocessing import Process, Lock
import jellyfish as jf
import time
#x="SakawISatamAtramtuprayARebrahmavAdinAm"
global mx,ctr,st,ans,dictt
mx=0
dictt={}
it= open("truth.txt",'r')
ct=0
for line in it:
	line=line.rstrip('\n')
        dictt[line]=ct
	ct+=1
#ctr=0
it.close()
it=open("truth.txt",'r')

#rdf= open("modslok.txt",'r')
st=""
#with open("modslok.txt") as mf:
# rd=[next(mf) for x in xrange(3)] 
#print(rd)
#wr= open('linenos.txt','a')
ans=""
start_time=time.time()

def f(ss,es,ctr,lctr):
 wr=open(ctr,'w')
 #l.acquire()	
 mx=0

 st=""
 rd=[]	
 #for inp in rds:
 with open("mods2.txt") as inp:
 	for x1 in xrange(2*ss):
 	    try:
         	next(inp)
            except StopIteration:
                break
 	for xx in xrange(2*(es-ss)+1):
           try: 
            rd.append(next(inp))	
           except StopIteration:
            break
 
 for line in rd:
    if line == '\n':
      continue
    wr.write(str(lctr))
    wr.flush()
    wr.write(' ')
    wr.flush()
    lctr+=1    
    for c in line:
         if ord(c)==32:
           continue 

                
                
	 elif ord(c)==124:
           if st!="":
            it=open("truth.txt",'r')
	    for ln in it:
                              
				sc=jf.jaro_winkler(unicode(ln.lower()),unicode(st.lower()))
				if sc>mx:
					mx=sc
					ans=ln
                        
			
            ans=ans.rstrip('\n')
            #print(ans)
            wr.write(str(dictt[ans]))
            wr.flush()
            wr.write(',')
            wr.flush()
	    ans=""
	    st=""
	    mx=0
            it.close()
	 else:
		    st+=c
    wr.write('\n')
    wr.flush()	
 #l.release()	    
 wr.close()
if __name__ == '__main__':
	#wr=open("linenos.txt",'a')
        #lock= Lock()
        ii=0
        lctr=0
	for lp in xrange(0,18288,381):
                ctr='storg'+str(ii);
                lctr+=381
                ii+=1
                #wr=open("linenos.txt",'a')
             
		Process(target=f, args=(lp,lp+380,ctr,lctr)).start()
               
              
        print("---%s seconds"%(time.time()-start_time))		
        
it.close()
#rdf.close()
#wr.close()
		




