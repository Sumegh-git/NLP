from multiprocessing import Process, Lock
import jellyfish as jf
import time

global mx,ctr,st,ans,dictt
mx=0
dictt={}
it= open("truth.txt",'r')
ctr=0
for line in it:
	line=line.rstrip('\n')
        dictt[line]=ctr
	ctr+=1
ctr=0
it.close()
it=open("truth.txt",'r')

#rdf= open("modslok.txt",'r')
st=""
#with open("modslok.txt") as mf:
# rd=[next(mf) for x in xrange(3)] 
#print(rd)
wr= open('linenos.txt','a')
ans=""
start_time=time.time()

def f(l,ss,es,ctr):
 l.acquire()	
 mx=0

 st=""
 rd=[]	
 #for inp in rds:
 with open("modslok.txt") as inp:
 	for x1 in xrange(2*ss):
 		next(inp)
 	rd=[next(inp) for xx in xrange(2*(es-ss)+1)]	

 
 for line in rd:
    if line == '\n':
      continue
    wr.write(str(ctr))
    wr.flush()
    wr.write(' ')
    wr.flush()
    ctr+=1    
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
 l.release()	    

if __name__ == '__main__':
	#wr=open("linenos.txt",'a')
        lock= Lock()
 
	for lp in xrange(0,18288,381):
                ctr=lp
                #wr=open("linenos.txt",'a')
             
		Process(target=f, args=(lock,lp,lp+380,ctr)).start()
               
              
        print("---%s seconds"%(time.time()-start_time))		
        
it.close()
#rdf.close()
wr.close()
		




