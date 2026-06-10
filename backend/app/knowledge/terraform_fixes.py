TERRAFORM_FIXES = [

    {
        "error": "image_id",
        "fix": """
OCI source_details block uses:

source_type = "image"
source_id   = IMAGE_OCID

Never use image_id.
"""
    },

    {
        "error": "sort_by",
        "fix": """
OCI data source supports:

TIMECREATED
DISPLAYNAME

Never use time_created.
"""
    },

    {
        "error": "is_hybrid",
        "fix": """
Remove is_hybrid.

This argument is unsupported.
"""
    },

    {
        "error": "free_text_search",
        "fix": """
free_text_search is unsupported.

Remove it completely.
"""
    }

]
