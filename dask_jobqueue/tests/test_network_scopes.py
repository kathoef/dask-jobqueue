import dask_jobqueue, pytest

def test_allow_locally_non_existent_worker_interface():
    """This ensures that setting an interface that is only available on compute nodes is possible. This interface should never be evaluated elsewhere."""
    with dask_jobqueue.SLURMCluster(
        cores=8, memory='24GB',
        interface='locally-non-existent-interface')
    as cluster:
        pass

def test_if_non_existent_interface_is_correctly_passed_to_job_script():
    """This ensures that the locally non-existent interface is correctly passed to the job script. IP address retrieval for the interface should happen with the Dask worker call."""
    with dask_jobqueue.SLURMCluster(
        cores=8, memory='24GB',
        interface='locally-non-existent-interface')
    as cluster:
        job_script = cluster.job_script()
        assert "locally-non-existent-interface" in job_script
