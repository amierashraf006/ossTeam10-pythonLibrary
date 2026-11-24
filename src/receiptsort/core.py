"""Core functions for receiptsort financial document extraction."""

from pathlib import Path
from typing import List, Literal
from pydantic import BaseModel, Field


class FinancialDocument(BaseModel):
    """Structured schema representing a single extracted financial transaction."""

    Date: str = Field(description="Transaction date in YYYY-MM-DD format.")
    Time: str = Field(description="Transaction time in HH:MM format, or '--:--'.")
    Receipt_Number: str = Field(description="Receipt, invoice, or reference number.")
    Type: Literal[
        "Cash Bill", "Receipt", "Cheque Stub", "Payment Voucher",
        "Petty Cash Voucher", "Cash Register Slip", "Bank Slip",
        "Money Transfer Slip", "Electronic Banking Slip", "Online Transaction",
        "Debit Advice", "Credit Advice", "Memorandum", "Invoice",
        "Debit Note", "Credit Note", "Utility Bill", "Customer Folio", "Other"
    ]
    Vendor: str = Field(description="Merchant, bank, or issuer name.")
    Category: Literal[
        "Transportation", "Food & Dining", "Utilities", "Office & Supplies",
        "IT & Hardware", "Banking & Finance", "Accommodation", "Other"
    ]
    Sub_Category: str = Field(description="Specific expense sub-category.")
    Subtotal: float = Field(description="Amount before tax.")
    Tax: float = Field(description="Total tax amount.")
    Total_Amount: float = Field(description="Grand total amount.")
    Currency: str = Field(description="3-letter ISO currency code.")
    Payment_Method: str = Field(description="Payment method used.")
    AI_Inferred: Literal["Yes", "No"] = Field(description="'Yes' if category was inferred.")


class DocumentBatch(BaseModel):
    """Batch container holding multiple extracted financial documents."""

    items: List[FinancialDocument]


def extract_zip(zip_path: str | Path, extract_dir: str | Path) -> List[Path]:
    """Extract supported financial document files from a ZIP archive.

    Args:
        zip_path (str | Path): Path to the input .zip file.
        extract_dir (str | Path): Directory where extracted files will be saved.

    Returns:
        List[Path]: List of paths to valid extracted document files.

    Raises:
        FileNotFoundError: If ``zip_path`` does not exist.

    Examples:
        >>> files = extract_zip("samples.zip", "temp_docs")
        >>> isinstance(files, list)
        True
    """
    raise NotImplementedError


def parse_document(file_path: str | Path) -> List[dict]:
    """Extract and categorize financial transactions from a single file using Gemini.

    Args:
        file_path (str | Path): Path to an image, PDF, CSV, or Excel file.

    Returns:
        List[dict]: Extracted transaction records matching ``FinancialDocument``.

    Raises:
        ValueError: If the file extension is not supported.

    Examples:
        >>> records = parse_document("receipt.jpg")
        >>> "Total_Amount" in records[0]
        True
    """
    raise NotImplementedError


def export_to_excel(records: List[dict], output_path: str | Path) -> Path:
    """Save extracted financial records into a formatted master Excel file.

    Args:
        records (List[dict]): List of transaction dictionaries to export.
        output_path (str | Path): Destination path for the output .xlsx file.

    Returns:
        Path: Path to the newly generated Excel spreadsheet.

    Raises:
        ValueError: If ``records`` is empty.

    Examples:
        >>> out = export_to_excel([{"Vendor": "Grab", "Total_Amount": 15.0}], "out.xlsx")
        >>> out.name
        'out.xlsx'
    """
    raise NotImplementedError