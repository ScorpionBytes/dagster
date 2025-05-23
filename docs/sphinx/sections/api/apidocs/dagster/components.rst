.. currentmodule:: dagster

Components
==========

Using Components
----------------

.. autodecorator:: component


.. autoclass:: ComponentLoadContext
   :members:


Building Components
-------------------

.. autoclass:: Component
    :members:


.. autoclass:: Resolvable
    :members:


.. autoclass:: ResolutionContext
    :members:


.. autoclass:: Resolver
    :members:


.. autoclass:: Model
    :members:


Core Models
-----------

These Annotated TypeAliases can be used when defining custom Components for
common dagster types.


.. py:data:: ResolvedAssetKey
    :type: Annotated[AssetKey, ...]

    Allows resolving to an AssetKey via a yaml friendly schema.

.. py:data:: ResolvedAssetSpec
    :type: Annotated[AssetSpec, ...]

    Allows resolving to an AssetSpec via a yaml friendly schema.

.. py:data:: AssetAttributesModel

    A pydantic modeling of all the attributes of an AssetSpec that can be set before the definition is created.

.. py:data:: ResolvedAssetCheckSpec
    :type: Annotated[AssetCheckSpec, ...]

    Allows resolving to an AssetCheckSpec via a yaml friendly schema.

.. autoclass:: AssetPostProcessorModel
