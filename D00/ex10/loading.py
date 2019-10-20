import time


def ft_progress(list) :
    size = len(list)
    start = time.time()
    for i in list:
        elapsed = time.time() - start
        percent = int((i / size) * 100)
        arrow_size =  int((i / size) * 20)
        eta = str(round(elapsed * 100 / ((i + 1) / size * 100), 2))
        begin_bar = "ETA: " + eta + "s [ " + str(percent) + "%]["
        bar = begin_bar + ("=" * arrow_size) + ">"
        bar = bar.ljust(len(begin_bar) + 20, ' ')
        bar = bar + "] " + str(i)+ "/100 | elapsed time " + str(round(elapsed, 2)) + "s"
        print(bar)
        yield bar


list = range(100)
for elem in ft_progress(list):
    time.sleep(0.01)