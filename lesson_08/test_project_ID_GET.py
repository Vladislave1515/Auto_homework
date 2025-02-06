import pytest
from YouGileAPI.projects_api import ProjectAPI

project_api = ProjectAPI(
    token='zdxJCD1R3GOMO7Pt3Ncu3Di0rjxiy0bni2Z-es-OwA7fwhr2sBZkGjMNRlR8k8y5'
)


@pytest.mark.run(order=3)
def test_get_project_by_id_positive():
    project_api.get_and_check_first_project()


@pytest.mark.run(order=3)
def test_get_project_by_invalid_id_negative():
    project_api.check_get_project_by_invalid_id('invalid_id')


@pytest.mark.run(order=3)
def test_get_project_by_nonexistent_id_negative():
    project_api.check_get_project_by_nonexistent_id(
        '4f6f3091-0f94-4d30-9b0e-99430a36d4fb'
    )


if __name__ == '__main__':
    pytest.main()
