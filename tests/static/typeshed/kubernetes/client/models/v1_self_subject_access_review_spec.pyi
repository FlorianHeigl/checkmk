# Stubs for kubernetes.client.models.v1_self_subject_access_review_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1SelfSubjectAccessReviewSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    non_resource_attributes: Any = ...
    resource_attributes: Any = ...
    def __init__(self, non_resource_attributes: Optional[Any] = ..., resource_attributes: Optional[Any] = ...) -> None: ...
    @property
    def non_resource_attributes(self): ...
    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes: Any) -> None: ...
    @property
    def resource_attributes(self): ...
    @resource_attributes.setter
    def resource_attributes(self, resource_attributes: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...