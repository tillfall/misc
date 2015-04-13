import os

dirs = ["c:\\movie\\被嫌弃的松子的一生",
    "c:\\movie"]

def ld(d):
    files = os.listdir(d)
    ret = []
    for file in files:
        ret.append(os.path.join(d, file))
    return ret
    
if '__main__' == __name__:
    '''
    for d in dirs:
        print()
        for f in ld(d):
            print(f)
            '''
    rep = [
        ['b被嫌弃的松子的一生.chn.srt', '被嫌弃的松子的一生.chn.srt'],
        ['b被嫌弃的松子的一生.chn1.srt', '被嫌弃的松子的一生.chn1.srt'],
        ['b被嫌弃的松子的一生.chn2.srt', '被嫌弃的松子的一生.chn2.srt'],
        ['b被嫌弃的松子的一生.mkv', '被嫌弃的松子的一生.mkv'],
        ]
    dir = 'c:\movie\被嫌弃的松子的一生'
    for x in rep:
        os.rename(os.path.join(dir, x[0]), os.path.join(dir, x[1]))