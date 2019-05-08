import multiprocessing as mupr
def pro1(pipe):
    pipe.send("hello")
    print("proc1 rec:",pipe.recv())
    
def pro2(pipe):
    print("proc2 rec:",pipe.recv())

pipe = mupr.Pipe()
p1 = mupr.Process(target = pro1,args=(pipe[0],))
p2 = mupr.Process(target = pro2,args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()