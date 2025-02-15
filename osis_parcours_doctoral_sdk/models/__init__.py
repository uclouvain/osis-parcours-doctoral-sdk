# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_parcours_doctoral_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.action_link import ActionLink
from osis_parcours_doctoral_sdk.model.ajouter_membre_command import AjouterMembreCommand
from osis_parcours_doctoral_sdk.model.categorie_activite import CategorieActivite
from osis_parcours_doctoral_sdk.model.choix_type_epreuve import ChoixTypeEpreuve
from osis_parcours_doctoral_sdk.model.communication import Communication
from osis_parcours_doctoral_sdk.model.complete_confirmation_paper_by_promoter_command import CompleteConfirmationPaperByPromoterCommand
from osis_parcours_doctoral_sdk.model.conference import Conference
from osis_parcours_doctoral_sdk.model.conference_communication import ConferenceCommunication
from osis_parcours_doctoral_sdk.model.conference_publication import ConferencePublication
from osis_parcours_doctoral_sdk.model.confirmation_paper_canvas import ConfirmationPaperCanvas
from osis_parcours_doctoral_sdk.model.confirmation_paper_dto import ConfirmationPaperDTO
from osis_parcours_doctoral_sdk.model.confirmation_paper_dto_demande_prolongation import ConfirmationPaperDTODemandeProlongation
from osis_parcours_doctoral_sdk.model.contexte_formation import ContexteFormation
from osis_parcours_doctoral_sdk.model.course import Course
from osis_parcours_doctoral_sdk.model.dashboard import Dashboard
from osis_parcours_doctoral_sdk.model.dashboard_links import DashboardLinks
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.doctoral_training_assent import DoctoralTrainingAssent
from osis_parcours_doctoral_sdk.model.doctoral_training_batch import DoctoralTrainingBatch
from osis_parcours_doctoral_sdk.model.doctoral_training_config import DoctoralTrainingConfig
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.external_supervision_dto import ExternalSupervisionDTO
from osis_parcours_doctoral_sdk.model.external_supervision_dto_parcours_doctoral import ExternalSupervisionDTOParcoursDoctoral
from osis_parcours_doctoral_sdk.model.external_supervision_dto_parcours_doctoral_projet import ExternalSupervisionDTOParcoursDoctoralProjet
from osis_parcours_doctoral_sdk.model.external_supervision_dto_supervision import ExternalSupervisionDTOSupervision
from osis_parcours_doctoral_sdk.model.inline_response200 import InlineResponse200
from osis_parcours_doctoral_sdk.model.inline_response2001 import InlineResponse2001
from osis_parcours_doctoral_sdk.model.inline_response2002 import InlineResponse2002
from osis_parcours_doctoral_sdk.model.jury_dto import JuryDTO
from osis_parcours_doctoral_sdk.model.jury_dto_membres import JuryDTOMembres
from osis_parcours_doctoral_sdk.model.jury_identity_dto import JuryIdentityDTO
from osis_parcours_doctoral_sdk.model.membre_jury_dto import MembreJuryDTO
from osis_parcours_doctoral_sdk.model.membre_jury_identity_dto import MembreJuryIdentityDTO
from osis_parcours_doctoral_sdk.model.modifier_cotutelle_command import ModifierCotutelleCommand
from osis_parcours_doctoral_sdk.model.modifier_financement_command import ModifierFinancementCommand
from osis_parcours_doctoral_sdk.model.modifier_jury_command import ModifierJuryCommand
from osis_parcours_doctoral_sdk.model.modifier_membre_command import ModifierMembreCommand
from osis_parcours_doctoral_sdk.model.modifier_role_membre_command import ModifierRoleMembreCommand
from osis_parcours_doctoral_sdk.model.paper import Paper
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto import ParcoursDoctoralDTO
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto_cotutelle import ParcoursDoctoralDTOCotutelle
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto_financement import ParcoursDoctoralDTOFinancement
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto_financement_bourse_recherche import ParcoursDoctoralDTOFinancementBourseRecherche
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto_links import ParcoursDoctoralDTOLinks
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto_projet import ParcoursDoctoralDTOProjet
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto import ParcoursDoctoralRechercheDTO
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto_formation import ParcoursDoctoralRechercheDTOFormation
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto_formation_campus import ParcoursDoctoralRechercheDTOFormationCampus
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto_formation_entite_gestion import ParcoursDoctoralRechercheDTOFormationEntiteGestion
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto_links import ParcoursDoctoralRechercheDTOLinks
from osis_parcours_doctoral_sdk.model.person import Person
from osis_parcours_doctoral_sdk.model.publication import Publication
from osis_parcours_doctoral_sdk.model.residency import Residency
from osis_parcours_doctoral_sdk.model.residency_communication import ResidencyCommunication
from osis_parcours_doctoral_sdk.model.scholarship import Scholarship
from osis_parcours_doctoral_sdk.model.seminar import Seminar
from osis_parcours_doctoral_sdk.model.seminar_communication import SeminarCommunication
from osis_parcours_doctoral_sdk.model.service import Service
from osis_parcours_doctoral_sdk.model.statut_activite import StatutActivite
from osis_parcours_doctoral_sdk.model.submit_confirmation_paper_command import SubmitConfirmationPaperCommand
from osis_parcours_doctoral_sdk.model.submit_confirmation_paper_extension_request_command import SubmitConfirmationPaperExtensionRequestCommand
from osis_parcours_doctoral_sdk.model.supervision_dto import SupervisionDTO
from osis_parcours_doctoral_sdk.model.supervision_dto_promoteur import SupervisionDTOPromoteur
from osis_parcours_doctoral_sdk.model.supervision_dto_signatures_membres_ca import SupervisionDTOSignaturesMembresCA
from osis_parcours_doctoral_sdk.model.supervision_dto_signatures_promoteurs import SupervisionDTOSignaturesPromoteurs
from osis_parcours_doctoral_sdk.model.tutor import Tutor
from osis_parcours_doctoral_sdk.model.ucl_course import UclCourse
from osis_parcours_doctoral_sdk.model.valorisation import Valorisation
