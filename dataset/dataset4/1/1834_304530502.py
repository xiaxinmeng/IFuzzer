os.register_at_fork(before=prepare_for_launch,
                    after_parent=launch_cleanup,
                    after_child=reinitialize_stuff)