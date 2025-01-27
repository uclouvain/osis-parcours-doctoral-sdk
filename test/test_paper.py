"""
    Parcours Doctoral API

    This API delivers data for the Parcours Doctoral project.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.model.categorie_activite import CategorieActivite
from osis_parcours_doctoral_sdk.model.choix_type_epreuve import ChoixTypeEpreuve
from osis_parcours_doctoral_sdk.model.contexte_formation import ContexteFormation
from osis_parcours_doctoral_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['ChoixTypeEpreuve'] = ChoixTypeEpreuve
globals()['ContexteFormation'] = ContexteFormation
globals()['StatutActivite'] = StatutActivite
from osis_parcours_doctoral_sdk.model.paper import Paper


class TestPaper(unittest.TestCase):
    """Paper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaper(self):
        """Test Paper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Paper()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
