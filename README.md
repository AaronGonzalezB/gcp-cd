# gcp-cd

## 1. Demo of Continuous Delivery with GCP

1. Create a new in GCP - gcp-cd
2. Open the console, verify that the gcp-cd is connected to the Terminal
3. Create a SSH Key to clone the Github repo
4. Project structure:

    * Makefile
    * Requirements.txt
    * app.yaml
    * main.py
    * main_test.py
    * cloudbuild.yaml

5. Set up a virtual environment: `virtualenv --python $(which python3) ~/.gcp-cd`
6. Activate the venv: `source ~/.gcp-cd/bin/activate`
7. Execute makefile process: `make install`

* You can view the details of your project with: `gcloud projects describe $GOOGLE_CLOUD_PROJECT`
* Also you can update your project: `gcloud config set project $GOOGLE_CLOUD_PROJECT`

8. Create an App from your Project: `gcloud app create`
9. Select a region, for this application we use us-central: `17`

#### Test Locally
10. Test your project locally: `python main.py`

You can Preview your development with the option "Web Preview" from the Cloud Shell Menu or with your localhost `http://127.0.0.1:8080/`

After you test your app and everything is fine, you can deploy into production.

#### Deployment
First of all, you have to Enable and create Cloudbuild Trigger into GCP: https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories

With the APIs enabled and the Trigger have been created, you can continue with the Terminal:

11. Deploy your app: `gcloud app deploy`

Copy the link of the deployed service.

12. Enable log entries in the app: `gcloud app logs tail -s default`
13. Add, commit and push the project to the Github Repo.\

Dont forget your credentials if it was the first time:

`git config --global user.email "you@example.com"`

`git config --global user.name "Your Name"`

Test with the URL provided by the deploy and thats all!
 
 If everything is ok until now, you have builded a CI/CD Hello World app!
 
 ## 2. Infrastructure as Code (IaS) with Terraform
 
 To setting up a VM with Terraform, in the Cloud Shell:
 
 * Create a terraform instance - `touch instance.tf` with these example settings:

```
resource "google_compute_instance" "default" {
    project      = "ias-project-326902"
    name         = "terraform"
    machine_type = "n1-standard-1"
    zone         = "us-central1-a"

    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-9"
        }
    }

    network_interface {
        network = "default"
        access_config {

        }
    }
}
```
* Initialize the Terraform instance - `terraform init`.
* You have to enable the Compute Engine API to apply the instance.
* Apply the instance - `terraform apply` and `yes` to changes. 

