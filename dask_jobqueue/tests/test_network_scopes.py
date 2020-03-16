import dask_jobqueue, pytest, dask

def test_allow_locally_non_existent_worker_interface():
    """Ensure setting interface only available on a compute node is possible.
    This interface should never be evaluated in any other than the Dask worker
    network scope, i.e. the scheduler network location should be set independently.
    """
    with dask_jobqueue.SLURMCluster(
        cores=8, memory='24GB',
        interface='locally-non-existent-interface',
    ) as cluster:
        job_script = cluster.job_script()
        assert "locally-non-existent-interface" in job_script


def test_allow_locally_non_existent_worker_interface_via_config_file():
    """This ensures the above behaviour for passing the option via a jobqueue configuration file."""
    dask.config.set({'jobqueue.slurm.interface':'locally-non-existent-interface'})
    with dask_jobqueue.SLURMCluster(
        cores=8, memory='24GB',
    ) as cluster:
        job_script = cluster.job_script()
        assert "locally-non-existent-interface" in job_script