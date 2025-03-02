import pytest
import crudatalab


@pytest.mark.parametrize('dataset_id', ['IMFWEO2020Apr', 'CDIACTACHIINDUSAA'])
def test_metadata(get_client, dataset_id):
    assert crudatalab.dataset(dataset_id)['id'] == dataset_id
