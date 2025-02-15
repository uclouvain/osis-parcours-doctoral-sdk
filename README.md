# osis-parcours-doctoral-sdk
This API delivers data for the Parcours Doctoral project.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.1
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/uclouvain/osis](https://github.com/uclouvain/osis)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_parcours_doctoral_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_parcours_doctoral_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_parcours_doctoral_sdk
from pprint import pprint
from osis_parcours_doctoral_sdk.api import autocomplete_api
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.inline_response200 import InlineResponse200
from osis_parcours_doctoral_sdk.model.inline_response2001 import InlineResponse2001
from osis_parcours_doctoral_sdk.model.inline_response2002 import InlineResponse2002
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/parcours_doctoral
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_parcours_doctoral_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/parcours_doctoral"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_parcours_doctoral_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    search = "search_example" # str | The term to search the persons on (first or last name, or global id)
limit = 1 # int | Number of results to return per page. (optional)
offset = 1 # int | The initial index from which to return the results. (optional)
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.list_people(search, limit=limit, offset=offset, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling AutocompleteApi->list_people: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/parcours_doctoral*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutocompleteApi* | [**list_people**](docs/AutocompleteApi.md#list_people) | **GET** /autocomplete/person | 
*AutocompleteApi* | [**list_scholarships**](docs/AutocompleteApi.md#list_scholarships) | **GET** /autocomplete/scholarship | 
*AutocompleteApi* | [**list_tutors**](docs/AutocompleteApi.md#list_tutors) | **GET** /autocomplete/tutor | 
*DoctorateApi* | [**assent_training**](docs/DoctorateApi.md#assent_training) | **POST** /doctorate/{uuid}/training/assent | 
*DoctorateApi* | [**complete_confirmation_paper_by_promoter**](docs/DoctorateApi.md#complete_confirmation_paper_by_promoter) | **PUT** /doctorate/{uuid}/supervised_confirmation | 
*DoctorateApi* | [**create_doctoral_training**](docs/DoctorateApi.md#create_doctoral_training) | **POST** /doctorate/{uuid}/doctoral-training | 
*DoctorateApi* | [**create_jury_members**](docs/DoctorateApi.md#create_jury_members) | **POST** /doctorate/{uuid}/jury/members | 
*DoctorateApi* | [**destroy_training**](docs/DoctorateApi.md#destroy_training) | **DELETE** /doctorate/{uuid}/training/{activity_id} | 
*DoctorateApi* | [**list_complementary_training**](docs/DoctorateApi.md#list_complementary_training) | **GET** /doctorate/{uuid}/complementary-training | 
*DoctorateApi* | [**list_course_enrollment**](docs/DoctorateApi.md#list_course_enrollment) | **GET** /doctorate/{uuid}/course-enrollment | 
*DoctorateApi* | [**list_doctoral_training**](docs/DoctorateApi.md#list_doctoral_training) | **GET** /doctorate/{uuid}/doctoral-training | 
*DoctorateApi* | [**list_doctorates**](docs/DoctorateApi.md#list_doctorates) | **GET** /doctorate/list | 
*DoctorateApi* | [**list_jury_members**](docs/DoctorateApi.md#list_jury_members) | **GET** /doctorate/{uuid}/jury/members | 
*DoctorateApi* | [**list_supervised_doctorates**](docs/DoctorateApi.md#list_supervised_doctorates) | **GET** /doctorate/supervised-list | 
*DoctorateApi* | [**remove_jury_member**](docs/DoctorateApi.md#remove_jury_member) | **DELETE** /doctorate/{uuid}/jury/members/{member_uuid} | 
*DoctorateApi* | [**retrieve_confirmation_papers**](docs/DoctorateApi.md#retrieve_confirmation_papers) | **GET** /doctorate/{uuid}/confirmation | 
*DoctorateApi* | [**retrieve_cotutelle**](docs/DoctorateApi.md#retrieve_cotutelle) | **GET** /doctorate/{uuid}/cotutelle | 
*DoctorateApi* | [**retrieve_dashboard**](docs/DoctorateApi.md#retrieve_dashboard) | **GET** /doctorate/dashboard | 
*DoctorateApi* | [**retrieve_doctoral_training_config**](docs/DoctorateApi.md#retrieve_doctoral_training_config) | **GET** /doctorate/{uuid}/training/config | 
*DoctorateApi* | [**retrieve_external_doctorate_supervision**](docs/DoctorateApi.md#retrieve_external_doctorate_supervision) | **GET** /doctorate/{uuid}/supervision/external/{token} | 
*DoctorateApi* | [**retrieve_funding**](docs/DoctorateApi.md#retrieve_funding) | **GET** /doctorate/{uuid}/funding | 
*DoctorateApi* | [**retrieve_jury_member**](docs/DoctorateApi.md#retrieve_jury_member) | **GET** /doctorate/{uuid}/jury/members/{member_uuid} | 
*DoctorateApi* | [**retrieve_jury_preparation**](docs/DoctorateApi.md#retrieve_jury_preparation) | **GET** /doctorate/{uuid}/jury/preparation | 
*DoctorateApi* | [**retrieve_last_confirmation_paper**](docs/DoctorateApi.md#retrieve_last_confirmation_paper) | **GET** /doctorate/{uuid}/confirmation/last | 
*DoctorateApi* | [**retrieve_last_confirmation_paper_canvas**](docs/DoctorateApi.md#retrieve_last_confirmation_paper_canvas) | **GET** /doctorate/{uuid}/confirmation/last/canvas | 
*DoctorateApi* | [**retrieve_parcours_doctoral_dto**](docs/DoctorateApi.md#retrieve_parcours_doctoral_dto) | **GET** /doctorate/{uuid} | 
*DoctorateApi* | [**retrieve_project**](docs/DoctorateApi.md#retrieve_project) | **GET** /doctorate/{uuid}/project | 
*DoctorateApi* | [**retrieve_supervision**](docs/DoctorateApi.md#retrieve_supervision) | **GET** /doctorate/{uuid}/supervision | 
*DoctorateApi* | [**retrieve_training**](docs/DoctorateApi.md#retrieve_training) | **GET** /doctorate/{uuid}/training/{activity_id} | 
*DoctorateApi* | [**submit_confirmation_paper**](docs/DoctorateApi.md#submit_confirmation_paper) | **PUT** /doctorate/{uuid}/confirmation/last | 
*DoctorateApi* | [**submit_confirmation_paper_extension_request**](docs/DoctorateApi.md#submit_confirmation_paper_extension_request) | **POST** /doctorate/{uuid}/confirmation/last | 
*DoctorateApi* | [**submit_training**](docs/DoctorateApi.md#submit_training) | **POST** /doctorate/{uuid}/training/submit | 
*DoctorateApi* | [**update_cotutelle**](docs/DoctorateApi.md#update_cotutelle) | **PUT** /doctorate/{uuid}/cotutelle | 
*DoctorateApi* | [**update_funding**](docs/DoctorateApi.md#update_funding) | **PUT** /doctorate/{uuid}/funding | 
*DoctorateApi* | [**update_jury_member**](docs/DoctorateApi.md#update_jury_member) | **PUT** /doctorate/{uuid}/jury/members/{member_uuid} | 
*DoctorateApi* | [**update_jury_preparation**](docs/DoctorateApi.md#update_jury_preparation) | **POST** /doctorate/{uuid}/jury/preparation | 
*DoctorateApi* | [**update_role_jury_member**](docs/DoctorateApi.md#update_role_jury_member) | **PATCH** /doctorate/{uuid}/jury/members/{member_uuid} | 
*DoctorateApi* | [**update_training**](docs/DoctorateApi.md#update_training) | **PUT** /doctorate/{uuid}/training/{activity_id} | 
*ReferencesApi* | [**retrieve_scholarship**](docs/ReferencesApi.md#retrieve_scholarship) | **GET** /references/scholarship/{uuid} | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [ActionLink](docs/ActionLink.md)
 - [AjouterMembreCommand](docs/AjouterMembreCommand.md)
 - [CategorieActivite](docs/CategorieActivite.md)
 - [ChoixTypeEpreuve](docs/ChoixTypeEpreuve.md)
 - [Communication](docs/Communication.md)
 - [CompleteConfirmationPaperByPromoterCommand](docs/CompleteConfirmationPaperByPromoterCommand.md)
 - [Conference](docs/Conference.md)
 - [ConferenceCommunication](docs/ConferenceCommunication.md)
 - [ConferencePublication](docs/ConferencePublication.md)
 - [ConfirmationPaperCanvas](docs/ConfirmationPaperCanvas.md)
 - [ConfirmationPaperDTO](docs/ConfirmationPaperDTO.md)
 - [ConfirmationPaperDTODemandeProlongation](docs/ConfirmationPaperDTODemandeProlongation.md)
 - [ContexteFormation](docs/ContexteFormation.md)
 - [Course](docs/Course.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardLinks](docs/DashboardLinks.md)
 - [DoctoralTrainingActivity](docs/DoctoralTrainingActivity.md)
 - [DoctoralTrainingAssent](docs/DoctoralTrainingAssent.md)
 - [DoctoralTrainingBatch](docs/DoctoralTrainingBatch.md)
 - [DoctoralTrainingConfig](docs/DoctoralTrainingConfig.md)
 - [Error](docs/Error.md)
 - [ExternalSupervisionDTO](docs/ExternalSupervisionDTO.md)
 - [ExternalSupervisionDTOParcoursDoctoral](docs/ExternalSupervisionDTOParcoursDoctoral.md)
 - [ExternalSupervisionDTOParcoursDoctoralProjet](docs/ExternalSupervisionDTOParcoursDoctoralProjet.md)
 - [ExternalSupervisionDTOSupervision](docs/ExternalSupervisionDTOSupervision.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [JuryDTO](docs/JuryDTO.md)
 - [JuryDTOMembres](docs/JuryDTOMembres.md)
 - [JuryIdentityDTO](docs/JuryIdentityDTO.md)
 - [MembreJuryDTO](docs/MembreJuryDTO.md)
 - [MembreJuryIdentityDTO](docs/MembreJuryIdentityDTO.md)
 - [ModifierCotutelleCommand](docs/ModifierCotutelleCommand.md)
 - [ModifierFinancementCommand](docs/ModifierFinancementCommand.md)
 - [ModifierJuryCommand](docs/ModifierJuryCommand.md)
 - [ModifierMembreCommand](docs/ModifierMembreCommand.md)
 - [ModifierRoleMembreCommand](docs/ModifierRoleMembreCommand.md)
 - [Paper](docs/Paper.md)
 - [ParcoursDoctoralDTO](docs/ParcoursDoctoralDTO.md)
 - [ParcoursDoctoralDTOCotutelle](docs/ParcoursDoctoralDTOCotutelle.md)
 - [ParcoursDoctoralDTOFinancement](docs/ParcoursDoctoralDTOFinancement.md)
 - [ParcoursDoctoralDTOFinancementBourseRecherche](docs/ParcoursDoctoralDTOFinancementBourseRecherche.md)
 - [ParcoursDoctoralDTOLinks](docs/ParcoursDoctoralDTOLinks.md)
 - [ParcoursDoctoralDTOProjet](docs/ParcoursDoctoralDTOProjet.md)
 - [ParcoursDoctoralIdentityDTO](docs/ParcoursDoctoralIdentityDTO.md)
 - [ParcoursDoctoralRechercheDTO](docs/ParcoursDoctoralRechercheDTO.md)
 - [ParcoursDoctoralRechercheDTOFormation](docs/ParcoursDoctoralRechercheDTOFormation.md)
 - [ParcoursDoctoralRechercheDTOFormationCampus](docs/ParcoursDoctoralRechercheDTOFormationCampus.md)
 - [ParcoursDoctoralRechercheDTOFormationEntiteGestion](docs/ParcoursDoctoralRechercheDTOFormationEntiteGestion.md)
 - [ParcoursDoctoralRechercheDTOLinks](docs/ParcoursDoctoralRechercheDTOLinks.md)
 - [Person](docs/Person.md)
 - [Publication](docs/Publication.md)
 - [Residency](docs/Residency.md)
 - [ResidencyCommunication](docs/ResidencyCommunication.md)
 - [Scholarship](docs/Scholarship.md)
 - [Seminar](docs/Seminar.md)
 - [SeminarCommunication](docs/SeminarCommunication.md)
 - [Service](docs/Service.md)
 - [StatutActivite](docs/StatutActivite.md)
 - [SubmitConfirmationPaperCommand](docs/SubmitConfirmationPaperCommand.md)
 - [SubmitConfirmationPaperExtensionRequestCommand](docs/SubmitConfirmationPaperExtensionRequestCommand.md)
 - [SupervisionDTO](docs/SupervisionDTO.md)
 - [SupervisionDTOPromoteur](docs/SupervisionDTOPromoteur.md)
 - [SupervisionDTOSignaturesMembresCA](docs/SupervisionDTOSignaturesMembresCA.md)
 - [SupervisionDTOSignaturesPromoteurs](docs/SupervisionDTOSignaturesPromoteurs.md)
 - [Tutor](docs/Tutor.md)
 - [UclCourse](docs/UclCourse.md)
 - [Valorisation](docs/Valorisation.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_parcours_doctoral_sdk.apis and osis_parcours_doctoral_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_parcours_doctoral_sdk.api.default_api import DefaultApi`
- `from osis_parcours_doctoral_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.apis import *
from osis_parcours_doctoral_sdk.models import *
```

