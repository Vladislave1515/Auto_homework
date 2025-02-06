import pytest
from YouGileAPI.projects_api import ProjectAPI

project_api = ProjectAPI(
    token='zdxJCD1R3GOMO7Pt3Ncu3Di0rjxiy0bni2Z-es-OwA7fwhr2sBZkGjMNRlR8k8y5'
)


@pytest.mark.run(order=1)
def test_create_project_positive_system_role():
    project_api.create_project_with_roles(
        user_id='f92aabc1-2754-403d-a238-f722107e3595',
        roles=['admin', 'worker', 'observer', '-']
    )


@pytest.mark.run(order=1)
def test_create_project_positive_new_user_ID():
    project_api.create_project_with_new_user(
        new_user_id='81dd5eab-30c0-4905-a16a-e03e818b0204'
        )


@pytest.mark.run(order=1)
def test_create_project_negative_unvalid_user_ID():
    project_api.create_project_with_invalid_user_id(
        invalid_user_id='92bc1-2754-43d-a38-f72213595'
        )


@pytest.mark.run(order=1)
def test_create_project_negative_without_title():
    project_api.create_project_without_title(
        user_id='f92aabc1-2754-403d-a238-f722107e3595'
        )


@pytest.mark.run(order=1)
def test_create_project_negative_without_role():
    project_api.create_project_without_role(
        user_id='f92aabc1-2754-403d-a238-f722107e3595'
        )


@pytest.mark.run(order=1)
def test_create_project_negative_unvalid_json():
    project_api.create_project_with_invalid_json(
        user_id='f92aabc1-2754-403d-a238-f722107e3595'
        )


if __name__ == '__main__':
    pytest.main()
