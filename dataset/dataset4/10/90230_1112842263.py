import _opcode as stats
def main(loops, level):
    ...
    ...

    stats.init_specialization_stats() # Clear unrelated status information
    stats.enable_specialization_stats()
    for _ in range_it: # core loop of benchmark
        stream = io.StringIO()
        solve_file(board, strategy, order, stream)
        output = stream.getvalue()
        stream = None
    stats.disable_specialization_stats()
    print(stats.get_specialization_stats())# Print status information
    ...
    ...
    return dt