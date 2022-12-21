# Copyright (c) 2019 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.
from typing import Dict, Optional, Any

from ..BaseModel import BaseModel


class CloudError(BaseModel):
    """Class representing errors generated by the cloud servers, according to the JSON-API standard."""

    def __init__(self, id: str, code: str, title: str, http_status: str, detail: Optional[str] = None,
                 meta: Optional[Dict[str, Any]] = None, **kwargs) -> None:
        """Creates a new error object.

        :param id: Unique identifier for this particular occurrence of the problem.
        :param title: A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence
          of the problem, except for purposes of localization.
        :param code: An application-specific error code, expressed as a string value.
        :param detail: A human-readable explanation specific to this occurrence of the problem. Like title, this field's
          value can be localized.
        :param http_status: The HTTP status code applicable to this problem, converted to string.
        :param meta: Non-standard meta-information about the error, depending on the error code.
        """

        self.id = id
        self.code = code
        self.http_status = http_status
        self.title = title
        self.detail = detail
        self.meta = meta
        super().__init__(**kwargs)
