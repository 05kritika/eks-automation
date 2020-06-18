terraform {
 # required_version = "~> 0.10"
  backend "s3"{
    bucket                 = "kritika-terraform"
    region                 = "us-east-1"
    key                    = "backup.tf"
#    workspace_key_prefix   = ""
#    dynamodb_table         = ""
  }
}
