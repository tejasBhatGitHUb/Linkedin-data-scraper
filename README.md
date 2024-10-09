Objective: Create a workflow that extracts company data from an SQL database, enriches the data using the LinkedIn Bulk Data Scraper API, and stores the enriched data in a new table in the database.

### Workflow Explanation of the Django Code:

The code defines two API views using Django Rest Framework (DRF) to:
1. Paginate and retrieve a list of companies from the database.
2. Enrich company data from LinkedIn using an external API and store it in the database if not already present.

#### **1. `CompanyListView`: Pagination and Retrieval of Company Data**

- **Purpose:** 
   - This view handles the retrieval and pagination of the company data stored in the `Company` model.
   
- **Key Components:**
  - `CustomPagination`: This class extends the `PageNumberPagination` from DRF and sets a default page size of 2. The pagination query parameter is set to "page".
  - `CompanyListView`: This API view inherits both the pagination class and `APIView` to handle GET requests.

- **Workflow:**
  1. **Retrieve Companies:** 
     - The `get` method fetches all the company objects from the database using `Company.objects.all()`.
  2. **Paginate the Data:**
     - The `paginate_queryset` method paginates the data based on the page size and query parameters.
  3. **Serialize Data:**
     - The `CompanySerializer` converts the paginated company data into JSON format.
  4. **Return Paginated Response:**
     - The paginated response is returned, providing a specific subset of company data based on the page requested.

---

#### **2. `EnrichCompanyDataView`: Fetch and Store Enriched Company Data**

- **Purpose:**
   - This view enriches a company's data by fetching additional details from an external LinkedIn API, storing the enriched data in the database if it does not already exist.

- **Key Components:**
  - `EnrichedCompany`: A model that stores the enriched company data.
  - `Company`: A model that stores the basic company data, such as the LinkedIn URL.
  - **Environment Variables**: Used to securely store API keys and configuration details, loaded via `dotenv`.
  - **External API**: Interacts with the LinkedIn Bulk Data Scraper API to enrich the company data.

- **Workflow:**
  1. **Check for Existing Enriched Data:**
     - The `get` method takes a `company_id` as a parameter and tries to retrieve the enriched data from the `EnrichedCompany` model. If found, it returns the serialized enriched data.
  
  2. **If Enriched Data Doesn't Exist:**
     - If the enriched data is not found, the code will try to retrieve the basic company data from the `Company` model using the `company_id`.
  
  3. **Prepare and Send API Request:**
     - The LinkedIn URL of the company is used to create a payload.
     - The payload and the necessary headers (API key, host, etc.) are dynamically fetched from the `.env` file using `os.getenv()`.
     - A POST request is sent to the LinkedIn Bulk Data Scraper API using `requests.post()`.
  
  4. **Process API Response:**
     - If the API request is successful (HTTP 200), the response is parsed. The code extracts specific fields (like `specialities`, `tagline`, `industry`, etc.) from the response to filter only the required data.
  
  5. **Store Enriched Data:**
     - The filtered data is then used to create a new record in the `EnrichedCompany` model. The company object and the enriched data are saved into the database.
  
  6. **Return Response:**
     - The enriched company data is serialized and returned with a status of `201 Created` if the data was successfully stored. If the API request fails, a 500 error is returned. If the company isn't found, a 404 error is returned.

---

### Example Workflow Execution:

#### **Scenario 1: Retrieving Paginated Companies**
1. A GET request is made to the `CompanyListView` endpoint.
2. All companies are fetched from the `Company` model.
3. The data is paginated with a page size of 2.
4. The paginated data is serialized and returned as a response.

#### **Scenario 2: Enriching a Company**
1. A GET request is made to the `EnrichCompanyDataView` endpoint with a specific `company_id`.
2. The code checks if the enriched data for the given `company_id` already exists in the `EnrichedCompany` table.
   - If it exists, it returns the serialized enriched data.
3. If the data does not exist, it fetches the company information from the `Company` table using the `company_id`.
4. A POST request is made to the LinkedIn Bulk Data Scraper API with the company's LinkedIn URL.
5. The API response is parsed, filtering out unwanted fields.
6. The enriched data is stored in the `EnrichedCompany` table.
7. The serialized enriched data is returned with a status of `201 Created`.

---

### Key Features:

1. **Pagination:** Ensures that large datasets are broken down into manageable chunks.
2. **Dynamic Data Fetching:** Pulls enriched data from an external API only when necessary.
3. **Error Handling:** Provides appropriate responses based on different scenarios, like missing data or failed API requests.
4. **Security:** API keys and configuration are securely handled through environment variables.

This structure provides a robust and scalable way to manage company data, enriching it on-demand without redundancy.
