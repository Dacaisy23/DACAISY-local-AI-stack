resource "aws_s3_bucket" "caisy_bucket" {
  bucket = "caisy-secured-data-2026"
}

resource "aws_s3_bucket_public_access_block" "caisy_security" {
  bucket = aws_s3_bucket.caisy_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
