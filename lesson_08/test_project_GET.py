import pytest
from YouGileAPI.projects_api import ProjectAPI

project_api = ProjectAPI(
    token='zdxJCD1R3GOMO7Pt3Ncu3Di0rjxiy0bni2Z-es-OwA7fwhr2sBZkGjMNRlR8k8y5'
)


# Тест на получение всех проектов
@pytest.mark.run(order=2)
def test_get_projects():
    project_api.check_get_projects()


# Тест на получение проектов по заголовку
@pytest.mark.run(order=2)
def test_get_projects_with_title():
    project_api.check_get_projects_with_title('Проект 1')


# Тест на получение проектов с ограничением на количество
@pytest.mark.run(order=2)
def test_get_projects_with_limit():
    project_api.check_get_projects_with_limit(10)


# Тест на получение проектов с указанным сдвигом
@pytest.mark.run(order=2)
def test_get_projects_with_offset():
    project_api.check_get_projects_with_offset(10)


if __name__ == '__main__':
    pytest.main()
