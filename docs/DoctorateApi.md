# osis_parcours_doctoral_sdk.DoctorateApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/parcours_doctoral*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assent_training**](DoctorateApi.md#assent_training) | **POST** /doctorate/{uuid}/training/assent | 
[**complete_confirmation_paper_by_promoter**](DoctorateApi.md#complete_confirmation_paper_by_promoter) | **PUT** /doctorate/{uuid}/supervised_confirmation | 
[**create_doctoral_training**](DoctorateApi.md#create_doctoral_training) | **POST** /doctorate/{uuid}/doctoral-training | 
[**create_jury_members**](DoctorateApi.md#create_jury_members) | **POST** /doctorate/{uuid}/jury/members | 
[**destroy_training**](DoctorateApi.md#destroy_training) | **DELETE** /doctorate/{uuid}/training/{activity_id} | 
[**list_complementary_training**](DoctorateApi.md#list_complementary_training) | **GET** /doctorate/{uuid}/complementary-training | 
[**list_course_enrollment**](DoctorateApi.md#list_course_enrollment) | **GET** /doctorate/{uuid}/course-enrollment | 
[**list_doctoral_training**](DoctorateApi.md#list_doctoral_training) | **GET** /doctorate/{uuid}/doctoral-training | 
[**list_doctorates**](DoctorateApi.md#list_doctorates) | **GET** /doctorate/list | 
[**list_jury_members**](DoctorateApi.md#list_jury_members) | **GET** /doctorate/{uuid}/jury/members | 
[**list_supervised_doctorates**](DoctorateApi.md#list_supervised_doctorates) | **GET** /doctorate/supervised-list | 
[**remove_jury_member**](DoctorateApi.md#remove_jury_member) | **DELETE** /doctorate/{uuid}/jury/members/{member_uuid} | 
[**retrieve_confirmation_papers**](DoctorateApi.md#retrieve_confirmation_papers) | **GET** /doctorate/{uuid}/confirmation | 
[**retrieve_cotutelle**](DoctorateApi.md#retrieve_cotutelle) | **GET** /doctorate/{uuid}/cotutelle | 
[**retrieve_dashboard**](DoctorateApi.md#retrieve_dashboard) | **GET** /doctorate/dashboard | 
[**retrieve_doctoral_training_config**](DoctorateApi.md#retrieve_doctoral_training_config) | **GET** /doctorate/{uuid}/training/config | 
[**retrieve_external_doctorate_supervision**](DoctorateApi.md#retrieve_external_doctorate_supervision) | **GET** /doctorate/{uuid}/supervision/external/{token} | 
[**retrieve_funding**](DoctorateApi.md#retrieve_funding) | **GET** /doctorate/{uuid}/funding | 
[**retrieve_jury_member**](DoctorateApi.md#retrieve_jury_member) | **GET** /doctorate/{uuid}/jury/members/{member_uuid} | 
[**retrieve_jury_preparation**](DoctorateApi.md#retrieve_jury_preparation) | **GET** /doctorate/{uuid}/jury/preparation | 
[**retrieve_last_confirmation_paper**](DoctorateApi.md#retrieve_last_confirmation_paper) | **GET** /doctorate/{uuid}/confirmation/last | 
[**retrieve_last_confirmation_paper_canvas**](DoctorateApi.md#retrieve_last_confirmation_paper_canvas) | **GET** /doctorate/{uuid}/confirmation/last/canvas | 
[**retrieve_parcours_doctoral_dto**](DoctorateApi.md#retrieve_parcours_doctoral_dto) | **GET** /doctorate/{uuid} | 
[**retrieve_project**](DoctorateApi.md#retrieve_project) | **GET** /doctorate/{uuid}/project | 
[**retrieve_supervision**](DoctorateApi.md#retrieve_supervision) | **GET** /doctorate/{uuid}/supervision | 
[**retrieve_supervision_canvas**](DoctorateApi.md#retrieve_supervision_canvas) | **GET** /doctorate/{uuid}/supervision_canvas | 
[**retrieve_training**](DoctorateApi.md#retrieve_training) | **GET** /doctorate/{uuid}/training/{activity_id} | 
[**submit_confirmation_paper**](DoctorateApi.md#submit_confirmation_paper) | **PUT** /doctorate/{uuid}/confirmation/last | 
[**submit_confirmation_paper_extension_request**](DoctorateApi.md#submit_confirmation_paper_extension_request) | **POST** /doctorate/{uuid}/confirmation/last | 
[**submit_training**](DoctorateApi.md#submit_training) | **POST** /doctorate/{uuid}/training/submit | 
[**update_cotutelle**](DoctorateApi.md#update_cotutelle) | **PUT** /doctorate/{uuid}/cotutelle | 
[**update_funding**](DoctorateApi.md#update_funding) | **PUT** /doctorate/{uuid}/funding | 
[**update_jury_member**](DoctorateApi.md#update_jury_member) | **PUT** /doctorate/{uuid}/jury/members/{member_uuid} | 
[**update_jury_preparation**](DoctorateApi.md#update_jury_preparation) | **POST** /doctorate/{uuid}/jury/preparation | 
[**update_role_jury_member**](DoctorateApi.md#update_role_jury_member) | **PATCH** /doctorate/{uuid}/jury/members/{member_uuid} | 
[**update_training**](DoctorateApi.md#update_training) | **PUT** /doctorate/{uuid}/training/{activity_id} | 


# **assent_training**
> DoctoralTrainingAssent assent_training(uuid, activity_id)



Assent on a doctoral training activity.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_assent import DoctoralTrainingAssent
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    activity_id = "activity_id_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    doctoral_training_assent = DoctoralTrainingAssent(
        approbation=True,
        commentaire="commentaire_example",
    ) # DoctoralTrainingAssent |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.assent_training(uuid, activity_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->assent_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.assent_training(uuid, activity_id, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, doctoral_training_assent=doctoral_training_assent)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->assent_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **activity_id** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **doctoral_training_assent** | [**DoctoralTrainingAssent**](DoctoralTrainingAssent.md)|  | [optional]

### Return type

[**DoctoralTrainingAssent**](DoctoralTrainingAssent.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_confirmation_paper_by_promoter**
> ParcoursDoctoralIdentityDTO complete_confirmation_paper_by_promoter(uuid)



Complete the confirmation paper related to a parcours_doctoral

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.complete_confirmation_paper_by_promoter_command import CompleteConfirmationPaperByPromoterCommand
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    complete_confirmation_paper_by_promoter_command = CompleteConfirmationPaperByPromoterCommand(
        proces_verbal_ca=[
            "proces_verbal_ca_example",
        ],
        avis_renouvellement_mandat_recherche=[
            "avis_renouvellement_mandat_recherche_example",
        ],
    ) # CompleteConfirmationPaperByPromoterCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.complete_confirmation_paper_by_promoter(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->complete_confirmation_paper_by_promoter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.complete_confirmation_paper_by_promoter(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, complete_confirmation_paper_by_promoter_command=complete_confirmation_paper_by_promoter_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->complete_confirmation_paper_by_promoter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **complete_confirmation_paper_by_promoter_command** | [**CompleteConfirmationPaperByPromoterCommand**](CompleteConfirmationPaperByPromoterCommand.md)|  | [optional]

### Return type

[**ParcoursDoctoralIdentityDTO**](ParcoursDoctoralIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_doctoral_training**
> DoctoralTrainingActivity create_doctoral_training(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    doctoral_training_activity = DoctoralTrainingActivity(None) # DoctoralTrainingActivity |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_doctoral_training(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->create_doctoral_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_doctoral_training(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, doctoral_training_activity=doctoral_training_activity)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->create_doctoral_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **doctoral_training_activity** | [**DoctoralTrainingActivity**](DoctoralTrainingActivity.md)|  | [optional]

### Return type

[**DoctoralTrainingActivity**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_jury_members**
> MembreJuryIdentityDTO create_jury_members(uuid)



Add a new member to the jury

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.ajouter_membre_command import AjouterMembreCommand
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.membre_jury_identity_dto import MembreJuryIdentityDTO
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    ajouter_membre_command = AjouterMembreCommand(
        matricule="matricule_example",
        institution="institution_example",
        autre_institution="autre_institution_example",
        pays="pays_example",
        nom="nom_example",
        prenom="prenom_example",
        titre="titre_example",
        justification_non_docteur="justification_non_docteur_example",
        genre="genre_example",
        email="email_example",
    ) # AjouterMembreCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_jury_members(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->create_jury_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_jury_members(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, ajouter_membre_command=ajouter_membre_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->create_jury_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **ajouter_membre_command** | [**AjouterMembreCommand**](AjouterMembreCommand.md)|  | [optional]

### Return type

[**MembreJuryIdentityDTO**](MembreJuryIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_training**
> destroy_training(uuid, activity_id)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    activity_id = "activity_id_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_training(uuid, activity_id)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->destroy_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.destroy_training(uuid, activity_id, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->destroy_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **activity_id** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_complementary_training**
> [DoctoralTrainingActivity] list_complementary_training(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_complementary_training(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_complementary_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_complementary_training(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_complementary_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[DoctoralTrainingActivity]**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_course_enrollment**
> [DoctoralTrainingActivity] list_course_enrollment(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_course_enrollment(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_course_enrollment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_course_enrollment(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_course_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[DoctoralTrainingActivity]**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_doctoral_training**
> [DoctoralTrainingActivity] list_doctoral_training(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_doctoral_training(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_doctoral_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_doctoral_training(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_doctoral_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[DoctoralTrainingActivity]**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_doctorates**
> [ParcoursDoctoralRechercheDTO] list_doctorates()



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto import ParcoursDoctoralRechercheDTO
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_doctorates(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_doctorates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[ParcoursDoctoralRechercheDTO]**](ParcoursDoctoralRechercheDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jury_members**
> [MembreJuryDTO] list_jury_members(uuid)



Get the members of a jury

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.membre_jury_dto import MembreJuryDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_jury_members(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_jury_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_jury_members(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_jury_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[MembreJuryDTO]**](MembreJuryDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supervised_doctorates**
> [ParcoursDoctoralRechercheDTO] list_supervised_doctorates()



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.parcours_doctoral_recherche_dto import ParcoursDoctoralRechercheDTO
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_supervised_doctorates(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->list_supervised_doctorates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[ParcoursDoctoralRechercheDTO]**](ParcoursDoctoralRechercheDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_jury_member**
> bool, date, datetime, dict, float, int, list, str, none_type remove_jury_member(uuid, member_uuid)



Remove a member

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_jury_member(uuid, member_uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->remove_jury_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_jury_member(uuid, member_uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->remove_jury_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_confirmation_papers**
> [ConfirmationPaperDTO] retrieve_confirmation_papers(uuid)



Get the confirmation papers related to the doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.confirmation_paper_dto import ConfirmationPaperDTO
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_confirmation_papers(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_confirmation_papers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_confirmation_papers(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_confirmation_papers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[ConfirmationPaperDTO]**](ConfirmationPaperDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_cotutelle**
> bool, date, datetime, dict, float, int, list, str, none_type retrieve_cotutelle(uuid)



This method is only used to check the permission. We have to return some data as the schema expects a 200 status and the deserializer expects some data.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_cotutelle(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_cotutelle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_cotutelle(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_cotutelle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dashboard**
> Dashboard retrieve_dashboard()



Get the actions links for the application

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.dashboard import Dashboard
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    search = "search_example" # str | A search term. (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_dashboard(ordering=ordering, search=search, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **search** | **str**| A search term. | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_doctoral_training_config**
> DoctoralTrainingConfig retrieve_doctoral_training_config(uuid)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_config import DoctoralTrainingConfig
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_doctoral_training_config(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_doctoral_training_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_doctoral_training_config(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_doctoral_training_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DoctoralTrainingConfig**](DoctoralTrainingConfig.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_external_doctorate_supervision**
> ExternalSupervisionDTO retrieve_external_doctorate_supervision(uuid, token)



Returns necessary info about the doctorate and the supervision.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.external_supervision_dto import ExternalSupervisionDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    token = "token_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_external_doctorate_supervision(uuid, token)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_external_doctorate_supervision: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_external_doctorate_supervision(uuid, token, accept_language=accept_language)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_external_doctorate_supervision: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **token** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]

### Return type

[**ExternalSupervisionDTO**](ExternalSupervisionDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_funding**
> bool, date, datetime, dict, float, int, list, str, none_type retrieve_funding(uuid)



This method is only used to check the permission. We have to return some data as the schema expects a 200 status and the deserializer expects some data.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_funding(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_funding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_funding(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_funding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_jury_member**
> MembreJuryDTO retrieve_jury_member(uuid, member_uuid)



Get the members of a jury

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.membre_jury_dto import MembreJuryDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_jury_member(uuid, member_uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_jury_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_jury_member(uuid, member_uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_jury_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**MembreJuryDTO**](MembreJuryDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_jury_preparation**
> JuryDTO retrieve_jury_preparation(uuid)



Get the Jury of a doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.jury_dto import JuryDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_jury_preparation(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_jury_preparation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_jury_preparation(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_jury_preparation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**JuryDTO**](JuryDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_last_confirmation_paper**
> ConfirmationPaperDTO retrieve_last_confirmation_paper(uuid)



Get the last confirmation paper related to the doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.confirmation_paper_dto import ConfirmationPaperDTO
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_last_confirmation_paper(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_last_confirmation_paper: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_last_confirmation_paper(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_last_confirmation_paper: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ConfirmationPaperDTO**](ConfirmationPaperDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_last_confirmation_paper_canvas**
> ConfirmationPaperCanvas retrieve_last_confirmation_paper_canvas(uuid)



Get the last confirmation paper canvas related to the doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.confirmation_paper_canvas import ConfirmationPaperCanvas
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_last_confirmation_paper_canvas(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_last_confirmation_paper_canvas: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_last_confirmation_paper_canvas(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_last_confirmation_paper_canvas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ConfirmationPaperCanvas**](ConfirmationPaperCanvas.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_parcours_doctoral_dto**
> ParcoursDoctoralDTO retrieve_parcours_doctoral_dto(uuid)



Get the parcours doctoral

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.parcours_doctoral_dto import ParcoursDoctoralDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_parcours_doctoral_dto(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_parcours_doctoral_dto: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_parcours_doctoral_dto(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_parcours_doctoral_dto: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ParcoursDoctoralDTO**](ParcoursDoctoralDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_project**
> bool, date, datetime, dict, float, int, list, str, none_type retrieve_project(uuid)



This method is only used to check the permission. We have to return some data as the schema expects a 200 status and the deserializer expects some data.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_project(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_project(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supervision**
> SupervisionDTO retrieve_supervision(uuid)



Get the supervision group of the PhD

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.supervision_dto import SupervisionDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_supervision(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_supervision: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_supervision(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_supervision: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**SupervisionDTO**](SupervisionDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supervision_canvas**
> SupervisionCanvas retrieve_supervision_canvas(uuid)



Get the supervision group of the PhD

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.supervision_canvas import SupervisionCanvas
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_supervision_canvas(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_supervision_canvas: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_supervision_canvas(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_supervision_canvas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**SupervisionCanvas**](SupervisionCanvas.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_training**
> DoctoralTrainingActivity retrieve_training(uuid, activity_id)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    activity_id = "activity_id_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_training(uuid, activity_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.retrieve_training(uuid, activity_id, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->retrieve_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **activity_id** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**DoctoralTrainingActivity**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_confirmation_paper**
> ParcoursDoctoralIdentityDTO submit_confirmation_paper(uuid)



Submit the last confirmation paper related to a doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_doctoral_sdk.model.submit_confirmation_paper_command import SubmitConfirmationPaperCommand
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    submit_confirmation_paper_command = SubmitConfirmationPaperCommand(
        date=dateutil_parser('1970-01-01').date(),
        rapport_recherche=[
            "rapport_recherche_example",
        ],
        proces_verbal_ca=[
            "proces_verbal_ca_example",
        ],
        avis_renouvellement_mandat_recherche=[
            "avis_renouvellement_mandat_recherche_example",
        ],
    ) # SubmitConfirmationPaperCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submit_confirmation_paper(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_confirmation_paper: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submit_confirmation_paper(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, submit_confirmation_paper_command=submit_confirmation_paper_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_confirmation_paper: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **submit_confirmation_paper_command** | [**SubmitConfirmationPaperCommand**](SubmitConfirmationPaperCommand.md)|  | [optional]

### Return type

[**ParcoursDoctoralIdentityDTO**](ParcoursDoctoralIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_confirmation_paper_extension_request**
> ParcoursDoctoralIdentityDTO submit_confirmation_paper_extension_request(uuid)



Submit the extension request of the last confirmation paper of a doctorate

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.submit_confirmation_paper_extension_request_command import SubmitConfirmationPaperExtensionRequestCommand
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    submit_confirmation_paper_extension_request_command = SubmitConfirmationPaperExtensionRequestCommand(
        nouvelle_echeance=dateutil_parser('1970-01-01').date(),
        justification_succincte="justification_succincte_example",
        lettre_justification=[
            "lettre_justification_example",
        ],
    ) # SubmitConfirmationPaperExtensionRequestCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submit_confirmation_paper_extension_request(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_confirmation_paper_extension_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submit_confirmation_paper_extension_request(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, submit_confirmation_paper_extension_request_command=submit_confirmation_paper_extension_request_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_confirmation_paper_extension_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **submit_confirmation_paper_extension_request_command** | [**SubmitConfirmationPaperExtensionRequestCommand**](SubmitConfirmationPaperExtensionRequestCommand.md)|  | [optional]

### Return type

[**ParcoursDoctoralIdentityDTO**](ParcoursDoctoralIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_training**
> DoctoralTrainingBatch submit_training(uuid)



Submit doctoral training activities.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_batch import DoctoralTrainingBatch
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    doctoral_training_batch = DoctoralTrainingBatch(
        activity_uuids=[
            "activity_uuids_example",
        ],
    ) # DoctoralTrainingBatch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.submit_training(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.submit_training(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, doctoral_training_batch=doctoral_training_batch)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->submit_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **doctoral_training_batch** | [**DoctoralTrainingBatch**](DoctoralTrainingBatch.md)|  | [optional]

### Return type

[**DoctoralTrainingBatch**](DoctoralTrainingBatch.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cotutelle**
> ParcoursDoctoralIdentityDTO update_cotutelle(uuid)



Set the cotutelle of the PhD.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.modifier_cotutelle_command import ModifierCotutelleCommand
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    modifier_cotutelle_command = ModifierCotutelleCommand(
        motivation="motivation_example",
        institution_fwb=True,
        institution="institution_example",
        autre_institution_nom="autre_institution_nom_example",
        autre_institution_adresse="autre_institution_adresse_example",
        demande_ouverture=[
            "demande_ouverture_example",
        ],
        convention=[
            "convention_example",
        ],
        autres_documents=[
            "autres_documents_example",
        ],
    ) # ModifierCotutelleCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_cotutelle(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_cotutelle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_cotutelle(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, modifier_cotutelle_command=modifier_cotutelle_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_cotutelle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **modifier_cotutelle_command** | [**ModifierCotutelleCommand**](ModifierCotutelleCommand.md)|  | [optional]

### Return type

[**ParcoursDoctoralIdentityDTO**](ParcoursDoctoralIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_funding**
> ParcoursDoctoralIdentityDTO update_funding(uuid)



Edit the project

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.parcours_doctoral_identity_dto import ParcoursDoctoralIdentityDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.modifier_financement_command import ModifierFinancementCommand
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    modifier_financement_command = ModifierFinancementCommand(
        type="type_example",
        type_contrat_travail="type_contrat_travail_example",
        eft=1,
        bourse_recherche="bourse_recherche_example",
        autre_bourse_recherche="autre_bourse_recherche_example",
        bourse_date_debut=dateutil_parser('1970-01-01').date(),
        bourse_date_fin=dateutil_parser('1970-01-01').date(),
        bourse_preuve=[
            "bourse_preuve_example",
        ],
        duree_prevue=1,
        temps_consacre=1,
        est_lie_fnrs_fria_fresh_csc=True,
        commentaire="commentaire_example",
    ) # ModifierFinancementCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_funding(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_funding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_funding(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, modifier_financement_command=modifier_financement_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_funding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **modifier_financement_command** | [**ModifierFinancementCommand**](ModifierFinancementCommand.md)|  | [optional]

### Return type

[**ParcoursDoctoralIdentityDTO**](ParcoursDoctoralIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jury_member**
> JuryIdentityDTO update_jury_member(uuid, member_uuid)



Update a member of the jury

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.jury_identity_dto import JuryIdentityDTO
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.modifier_membre_command import ModifierMembreCommand
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    modifier_membre_command = ModifierMembreCommand(
        matricule="matricule_example",
        institution="institution_example",
        autre_institution="autre_institution_example",
        pays="pays_example",
        nom="nom_example",
        prenom="prenom_example",
        titre="titre_example",
        justification_non_docteur="justification_non_docteur_example",
        genre="genre_example",
        email="email_example",
    ) # ModifierMembreCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_jury_member(uuid, member_uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_jury_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_jury_member(uuid, member_uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, modifier_membre_command=modifier_membre_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_jury_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **modifier_membre_command** | [**ModifierMembreCommand**](ModifierMembreCommand.md)|  | [optional]

### Return type

[**JuryIdentityDTO**](JuryIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jury_preparation**
> JuryIdentityDTO update_jury_preparation(uuid)



Update the jury preparation information

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.jury_identity_dto import JuryIdentityDTO
from osis_parcours_doctoral_sdk.model.modifier_jury_command import ModifierJuryCommand
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    modifier_jury_command = ModifierJuryCommand(
        titre_propose="titre_propose_example",
        formule_defense="formule_defense_example",
        date_indicative=dateutil_parser('1970-01-01').date(),
        langue_redaction="langue_redaction_example",
        langue_soutenance="langue_soutenance_example",
        commentaire="commentaire_example",
    ) # ModifierJuryCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_jury_preparation(uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_jury_preparation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_jury_preparation(uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, modifier_jury_command=modifier_jury_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_jury_preparation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **modifier_jury_command** | [**ModifierJuryCommand**](ModifierJuryCommand.md)|  | [optional]

### Return type

[**JuryIdentityDTO**](JuryIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_jury_member**
> JuryIdentityDTO update_role_jury_member(uuid, member_uuid)



Update the role of a member of the jury

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.jury_identity_dto import JuryIdentityDTO
from osis_parcours_doctoral_sdk.model.modifier_role_membre_command import ModifierRoleMembreCommand
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    modifier_role_membre_command = ModifierRoleMembreCommand(
        role="role_example",
    ) # ModifierRoleMembreCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_role_jury_member(uuid, member_uuid)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_role_jury_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_role_jury_member(uuid, member_uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, modifier_role_membre_command=modifier_role_membre_command)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_role_jury_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **modifier_role_membre_command** | [**ModifierRoleMembreCommand**](ModifierRoleMembreCommand.md)|  | [optional]

### Return type

[**JuryIdentityDTO**](JuryIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training**
> DoctoralTrainingActivity update_training(uuid, activity_id)



### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_doctoral_sdk
from osis_parcours_doctoral_sdk.api import doctorate_api
from osis_parcours_doctoral_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_parcours_doctoral_sdk.model.error import Error
from osis_parcours_doctoral_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
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
    api_instance = doctorate_api.DoctorateApi(api_client)
    uuid = "uuid_example" # str | 
    activity_id = "activity_id_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    doctoral_training_activity = DoctoralTrainingActivity(None) # DoctoralTrainingActivity |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_training(uuid, activity_id)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_training: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_training(uuid, activity_id, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, doctoral_training_activity=doctoral_training_activity)
        pprint(api_response)
    except osis_parcours_doctoral_sdk.ApiException as e:
        print("Exception when calling DoctorateApi->update_training: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **activity_id** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **doctoral_training_activity** | [**DoctoralTrainingActivity**](DoctoralTrainingActivity.md)|  | [optional]

### Return type

[**DoctoralTrainingActivity**](DoctoralTrainingActivity.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

