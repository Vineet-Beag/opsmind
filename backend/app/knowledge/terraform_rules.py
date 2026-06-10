RULES = """
Terraform Provider Rules:

OCI:

1. Use source_id instead of image_id inside source_details

Correct:

source_details {
  source_type = "image"
  source_id   = data.oci_core_images.oracle_linux_image.images[0].id
}

Wrong:

source_details {
  image_id = ...
}

----------------------------------------

2. Do not use is_hybrid on oci_core_vcn

----------------------------------------

3. sort_by must be:

TIMECREATED

or

DISPLAYNAME

Never:

time_created

----------------------------------------

4. Use provider source:

terraform {
  required_providers {
    oci = {
      source = "oracle/oci"
    }
  }
}

Never:

hashicorp/oci

----------------------------------------

5. Return ONLY JSON

Never markdown

Never use code fences.

Never return json wrapped in markdown.

Return:

{
  "main_tf": "...",
  "variables_tf": "...",
  "outputs_tf": "..."
}
"""
