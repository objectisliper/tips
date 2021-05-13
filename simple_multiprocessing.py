import multiprocessing

from billiard.context import Process


def str_target_executor(index: int, str_to_return: str, pipe) -> (int, str):
    pipe.send((index, str_to_return))


def process(text: str) -> list:
    pipe_return, pipe_receive = multiprocessing.Pipe(False)
    cpu_count = multiprocessing.cpu_count()
    process_list = []
    str_parts = text.split('_')
    for i in range(cpu_count):
        try:
            executor = Process(target=str_target_executor, args=(i, str_parts[i], pipe_receive))
            process_list.append(executor)
            executor.start()
        except IndexError:
            continue

    last_list = []
    for _ in process_list:
        index, str_part = pipe_return.recv()
        last_list.append((index, str_part))

    for executor in process_list:
        executor.join()

    print(last_list)
    last_list.sort(key=lambda a: a[0])
    print(' '.join(map(lambda a: a[1], last_list)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process('some_text_for_my_loolze')
