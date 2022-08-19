# Auto generated from config.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-19T09:57:53
# Schema: linter-config
#
# id: https://w3id.org/linkml/linter/config
# description: A datamodel describing the configuration file accepted by the linkml-lint command
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
import sys
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import JsonObj, as_dict
from linkml_runtime.linkml_model.meta import (EnumDefinition, PermissibleValue,
                                              PvFormulaOptions)
from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import \
    dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import camelcase, sfx, underscore
from linkml_runtime.utils.metamodelcore import (Bool, bnode, empty_dict,
                                                empty_list)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (YAMLRoot, extended_float,
                                            extended_int, extended_str)
from rdflib import Namespace, URIRef

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
LINTCFG = CurieNamespace("lintcfg", "https://w3id.org/linkml/linter/config")
DEFAULT_ = LINTCFG


# Types

# Class references


@dataclass
class Config(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINTCFG.Config
    class_class_curie: ClassVar[str] = "lintcfg:Config"
    class_name: ClassVar[str] = "Config"
    class_model_uri: ClassVar[URIRef] = LINTCFG.Config

    no_empty_title: Optional[Union[dict, "RuleConfig"]] = None
    permissible_values_format: Optional[
        Union[dict, "PermissibleValuesFormatRuleConfig"]
    ] = None
    tree_root_class: Optional[Union[dict, "TreeRootClassRuleConfig"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.no_empty_title is not None and not isinstance(
            self.no_empty_title, RuleConfig
        ):
            self.no_empty_title = RuleConfig(**as_dict(self.no_empty_title))

        if self.permissible_values_format is not None and not isinstance(
            self.permissible_values_format, PermissibleValuesFormatRuleConfig
        ):
            self.permissible_values_format = PermissibleValuesFormatRuleConfig(
                **as_dict(self.permissible_values_format)
            )

        if self.tree_root_class is not None and not isinstance(
            self.tree_root_class, TreeRootClassRuleConfig
        ):
            self.tree_root_class = TreeRootClassRuleConfig(
                **as_dict(self.tree_root_class)
            )

        super().__post_init__(**kwargs)


@dataclass
class RuleConfig(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINTCFG.RuleConfig
    class_class_curie: ClassVar[str] = "lintcfg:RuleConfig"
    class_name: ClassVar[str] = "RuleConfig"
    class_model_uri: ClassVar[URIRef] = LINTCFG.RuleConfig

    level: Union[str, "RuleLevel"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, RuleLevel):
            self.level = RuleLevel(self.level)

        super().__post_init__(**kwargs)


@dataclass
class PermissibleValuesFormatRuleConfig(RuleConfig):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINTCFG.PermissibleValuesFormatRuleConfig
    class_class_curie: ClassVar[str] = "lintcfg:PermissibleValuesFormatRuleConfig"
    class_name: ClassVar[str] = "PermissibleValuesFormatRuleConfig"
    class_model_uri: ClassVar[URIRef] = LINTCFG.PermissibleValuesFormatRuleConfig

    level: Union[str, "RuleLevel"] = None
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass
class TreeRootClassRuleConfig(RuleConfig):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINTCFG.TreeRootClassRuleConfig
    class_class_curie: ClassVar[str] = "lintcfg:TreeRootClassRuleConfig"
    class_name: ClassVar[str] = "TreeRootClassRuleConfig"
    class_model_uri: ClassVar[URIRef] = LINTCFG.TreeRootClassRuleConfig

    level: Union[str, "RuleLevel"] = None
    root_class_name: Optional[str] = None
    validate_existing_class_name: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.root_class_name is not None and not isinstance(
            self.root_class_name, str
        ):
            self.root_class_name = str(self.root_class_name)

        if self.validate_existing_class_name is not None and not isinstance(
            self.validate_existing_class_name, Bool
        ):
            self.validate_existing_class_name = Bool(self.validate_existing_class_name)

        super().__post_init__(**kwargs)


# Enumerations
class RuleLevel(EnumDefinitionImpl):

    disabled = PermissibleValue(
        text="disabled", description="The rule will not be checked"
    )
    warning = PermissibleValue(
        text="warning",
        description="A violation of a rule at this level is a minor issue that should be fixed",
    )
    error = PermissibleValue(
        text="error",
        description="A violation of a rule at this level is a major issue that must be fixed",
    )

    _defn = EnumDefinition(
        name="RuleLevel",
    )


# Slots
class slots:
    pass


slots.config__no_empty_title = Slot(
    uri=LINTCFG.no_empty_title,
    name="config__no_empty_title",
    curie=LINTCFG.curie("no_empty_title"),
    model_uri=LINTCFG.config__no_empty_title,
    domain=None,
    range=Optional[Union[dict, RuleConfig]],
)

slots.config__permissible_values_format = Slot(
    uri=LINTCFG.permissible_values_format,
    name="config__permissible_values_format",
    curie=LINTCFG.curie("permissible_values_format"),
    model_uri=LINTCFG.config__permissible_values_format,
    domain=None,
    range=Optional[Union[dict, PermissibleValuesFormatRuleConfig]],
)

slots.config__tree_root_class = Slot(
    uri=LINTCFG.tree_root_class,
    name="config__tree_root_class",
    curie=LINTCFG.curie("tree_root_class"),
    model_uri=LINTCFG.config__tree_root_class,
    domain=None,
    range=Optional[Union[dict, TreeRootClassRuleConfig]],
)

slots.ruleConfig__level = Slot(
    uri=LINTCFG.level,
    name="ruleConfig__level",
    curie=LINTCFG.curie("level"),
    model_uri=LINTCFG.ruleConfig__level,
    domain=None,
    range=Union[str, "RuleLevel"],
)

slots.permissibleValuesFormatRuleConfig__format = Slot(
    uri=LINTCFG.format,
    name="permissibleValuesFormatRuleConfig__format",
    curie=LINTCFG.curie("format"),
    model_uri=LINTCFG.permissibleValuesFormatRuleConfig__format,
    domain=None,
    range=Optional[str],
)

slots.treeRootClassRuleConfig__root_class_name = Slot(
    uri=LINTCFG.root_class_name,
    name="treeRootClassRuleConfig__root_class_name",
    curie=LINTCFG.curie("root_class_name"),
    model_uri=LINTCFG.treeRootClassRuleConfig__root_class_name,
    domain=None,
    range=Optional[str],
)

slots.treeRootClassRuleConfig__validate_existing_class_name = Slot(
    uri=LINTCFG.validate_existing_class_name,
    name="treeRootClassRuleConfig__validate_existing_class_name",
    curie=LINTCFG.curie("validate_existing_class_name"),
    model_uri=LINTCFG.treeRootClassRuleConfig__validate_existing_class_name,
    domain=None,
    range=Optional[Union[bool, Bool]],
)
