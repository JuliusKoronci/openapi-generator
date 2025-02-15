# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401
import uuid  # noqa: F401

from petstore_api import schemas  # noqa: F401


class Drawing(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
        
            @classmethod
            @property
            def mainShape(cls) -> typing.Type['Shape']:
                return Shape
        
            @classmethod
            @property
            def shapeOrNull(cls) -> typing.Type['ShapeOrNull']:
                return ShapeOrNull
        
            @classmethod
            @property
            def nullableShape(cls) -> typing.Type['NullableShape']:
                return NullableShape
            
            
            class shapes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
            
                    @classmethod
                    @property
                    def items(cls) -> typing.Type['Shape']:
                        return Shape
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Shape'], typing.List['Shape']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shapes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i) -> 'items':
                    return super().__getitem__(i)
        
        @classmethod
        @property
        def additional_properties(cls) -> typing.Type['Fruit']:
            return Fruit
    
    mainShape: 'Shape'
    shapeOrNull: 'ShapeOrNull'
    nullableShape: 'NullableShape'
    shapes: MetaOapg.properties.shapes

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        mainShape: typing.Union['Shape', schemas.Unset] = schemas.unset,
        shapeOrNull: typing.Union['ShapeOrNull', schemas.Unset] = schemas.unset,
        nullableShape: typing.Union['NullableShape', schemas.Unset] = schemas.unset,
        shapes: typing.Union[MetaOapg.properties.shapes, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'Fruit',
    ) -> 'Drawing':
        return super().__new__(
            cls,
            *args,
            mainShape=mainShape,
            shapeOrNull=shapeOrNull,
            nullableShape=nullableShape,
            shapes=shapes,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.fruit import Fruit
from petstore_api.model.nullable_shape import NullableShape
from petstore_api.model.shape import Shape
from petstore_api.model.shape_or_null import ShapeOrNull
