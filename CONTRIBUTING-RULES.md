# Contributing Rules

This guide provides guidelines for contributing to IT-Wallet Technical Documentation. Following these conventions ensures consistency across all documentation files.

## Table of Contents

- [Contributing Rules](#contributing-rules)
  - [Table of Contents](#table-of-contents)
  - [General Formatting and Editorial Conventions](#general-formatting-and-editorial-conventions)
  - [File Organization](#file-organization)
  - [Section Headers](#section-headers)
  - [Cross-References](#cross-references)
    - [Internal References](#internal-references)
      - [Referencing External Resources](#referencing-external-resources)
      - [Referencing RFC Documents](#referencing-rfc-documents)
      - [Important Syntax Notes](#important-syntax-notes)
  - [Figures and Images](#figures-and-images)
    - [Image Formats and Requirements](#image-formats-and-requirements)
    - [File Organization for Images](#file-organization-for-images)
    - [Adding Images to Documentation](#adding-images-to-documentation)
      - [SVG and PDF Images](#svg-and-pdf-images)
      - [PlantUML Diagrams](#plantuml-diagrams)
    - [Image Attributes](#image-attributes)
    - [Cross-Referencing Figures](#cross-referencing-figures)
  - [Tables](#tables)
    - [Table Requirements](#table-requirements)
    - [Row and Cell Formatting](#row-and-cell-formatting)
    - [Cross-Referencing Tables](#cross-referencing-tables)
  - [Non-Normative Examples](#non-normative-examples)
    - [Inline Code Examples](#inline-code-examples)
    - [External Code Files](#external-code-files)
  - [Notes and Warnings](#notes-and-warnings)

## General Formatting and Editorial Conventions

- **Encoding**: Files should be saved with UTF-8 encoding
- **Technical parameter names**, such as JSON fileds or HTTP parameters, must be enclosed in double backticks, i.e.: ``client_id``, ``redirect_uri``, ``authorization_details``.
- **Example URLs** in non-normative examples must use not real domains (such as ``example.org``, ``wallet-provider.example.org``) and must not reference real production URLs
- **File and path names**, use lowercase, and be separated by hyphens: ``credential-issuance.rst``, ``credential-issuance-endpoint.rst``
- **Titles**, use Title Case Style: Capitalize all major words in titles. Major words exclude articles (a, an, the), prepositions (on, in, of, etc.), coordinating conjunctions (and, or, but, etc.), and 'to'.

## File Organization

When creating multiple RST files:

1. Create a main index file (e.g., `credential-issuance.rst`)
2. Use the `toctree` directive to organize related files:

```rst
.. toctree::
  :caption: Table of Contents
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-endpoint.rst
```

Parameters:
- `:caption:` - add a caption to the toctree
- `:maxdepth:` - the depth level to display in the table of contents

## Section Headers

Use the following characters for section levels, maintaining this hierarchy:

```
Equal signs (=) for Sections
============================
 
Hyphens (-) for Subsections
---------------------------
 
Carets (^) for Subsubsections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Double quotes (") for Paragraphs
"""""""""""""""""""""""""""""""
 
Dots (.) for Subparagraphs 
..........................
```

Section headers must have the same number of underline/overline characters as at least the length of the header text.

## Cross-References

### Internal References

This Technical Documentation uses `sphinx.ext.autosectionlabel` with `autosectionlabel_prefix_document` set to `True`.   

Therefore, for cross-referencing within documents, use the `:ref:` role with the name of the document in which the section is referenced and the section tile, separated by a colon:

```rst
See :ref:`file-name:Section Title`.
```

#### Referencing External Resources

To reference external resources in your documentation:

1. **Basic reference** - use underscore suffix:
   ```rst
   See `OpenID4VCI`_ for more information.
   ```

2. **Reference to specific section** - include section information:
   ```rst
   See Section 7.2 of [`OpenID4VCI`_].
   ```

#### Referencing RFC Documents

RFC documents use a special role syntax that differs from regular external references:

```rst
As defined in :rfc:`7519`.
```

You can also reference specific sections within RFCs:

```rst
See :rfc:`6749#section-4.1.2.1`.
```

These references will automatically link to the appropriate RFC document without needing an entry in `common_definitions.rst`.

#### Important Syntax Notes

- The reference name (e.g., `OpenID4VCI`) is case-sensitive
- The trailing underscore (`_`) is required in the reference usage
- When using brackets, the backtick+text+backtick+underscore combination must be exact: [`text`_]
- Always use backticks (`) and not single quotes (') around reference names
- Reference definitions in `common_definitions.rst` start with `.. _` (dot dot space underscore)
- Avoid duplicate reference names as they will cause build warnings

## Figures and Images

This section describes how to include figures and images in the documentation, supporting both HTML and PDF output formats.

### Image Formats and Requirements

The documentation supports two main approaches for figures:

1. **Static Images** (SVG and PDF)
   - SVG format is required for HTML output
   - PDF format is required for LaTeX/PDF output
   - Both formats must be provided for each image
   - A tool is available in `./docs/utils/svg2pdf.py` to automatically convert SVG to PDF

2. **PlantUML Diagrams**
   - All architecture, component, or sequence diagrams must be created using PlantUML
   - PlantUML's official Standard Library (stdlib) may be used if required
   - For technical details about available libraries, refer to [PlantUML's official Standard Library Documentation](https://plantuml.com/stdlib)

The approaches are mutually exclusive - use either static images OR PlantUML diagrams for a given figure.

### File Organization for Images

Images must be organized in specific directories based on their format:

- **SVG images**: Store in `./docs/en/images/svg/`
- **PDF images**: Store in `./docs/en/images/pdf/`
- **PlantUML diagrams**: Store source files in `./docs/en/plantuml/` with `.puml` extension

### Adding Images to Documentation

#### SVG and PDF Images

For static images, use conditional directives to include the appropriate format based on the output target:

```rst
.. _fig_reference_name:

.. only:: format_html

  .. figure:: ./images/svg/diagram-name.svg
    :alt: Description of the diagram
    :width: 100%
    :align: center

    Caption text describing the figure.

.. only:: format_latex

  .. figure:: ./images/pdf/diagram-name.pdf
    :alt: Description of the diagram
    :width: 100%
    :align: center

    Caption text describing the figure.
```

#### PlantUML Diagrams

For PlantUML diagrams, use the `plantuml` directive:

```rst
.. _fig_reference_name:
.. plantuml:: plantuml/diagram-name.puml
    :width: 99%
    :align: center
    :alt: Description of the diagram
    :caption: `Caption text describing the figure. <https://www.plantuml.com/plantuml/svg/ENCODED-URL>`_
```

Note that for PlantUML diagrams:
- The `:caption:` attribute must include a link to the preview SVG on the PlantUML website
- You do not need to use the `only::` directives as Sphinx will handle the output format automatically

### Image Attributes

When working with figures, understand the difference between these key attributes:

- **:figwidth:** Controls the width of the entire figure block, including the caption and any padding. It defines how much horizontal space the figure occupies in the document layout.

- **:width:** Controls only the width of the image itself, not the entire figure block. Use this when you need to resize just the image while allowing the caption to potentially be wider.

Other useful figure attributes:
- **:height:** Controls the height of the image
- **:scale:** Scales the image (e.g., `:scale: 50%`)
- **:alt:** Provides alternative text for accessibility (REQUIRED)
- **:align:** Specifies the alignment of the figure (typically `center`)

### Cross-Referencing Figures

When a figure has a label defined, you can reference it from anywhere in the documentation:

```rst
As shown in :ref:`fig_reference_name`, the components interact through...
```

This will create a link to the figure with the caption text as the link text.

## Tables

Use the `list-table` directive for tables:

```rst
.. _table_reference_name:
.. list-table:: Table Title
    :widths: 20 60 20
    :header-rows: 1

    * - **Column 1 Header**
      - **Column 2 Header**
      - **Column 3 Header**
    * - Cell 1
      - Cell 2
      - Cell 3
```

Parameters:
- `:widths:` - relative widths of each column
- `:header-rows:` - number of header rows (usually 1)

### Table Requirements

- The `list-table` directive must be used for all tables (not grid tables or simple tables)
- Each table should have a label for cross-referencing (e.g., `.. _table_name:`). Use the prefix `_table_` followed by the reference table name
- Each table should have a title
- The following attributes are required:
  - `:widths:` - relative widths of each column (must match the number of columns)
  - `:header-rows:` - number of header rows (usually 1)
- Headers should be in bold format using double asterisks (`**Header Text**`)

### Row and Cell Formatting

- Each row begins with a `*` character
- Each cell within a row begins with a `-` character
- Cells can contain multiple paragraphs, lists, or other block elements
- For multi-line content in a cell, ensure proper indentation:

```rst
* - Cell 1
  - This cell has
    multiple lines
    of content
  - Cell 3
```

### Cross-Referencing Tables

When a table has a label defined, you can reference it from anywhere in the documentation:

```rst
As shown in :ref:`table_reference_name`, the parameters include...
```

This will create a link to the table with the table title as the link text. For more specific references, you can refer to a table with custom text:

```rst
See the :ref:`Table of Credential Offer parameters <table_reference_name>`.
```

## Non-Normative Examples

When providing non-normative examples:

1. Clearly label them as non-normative in the text
2. Store examples in separate files when possible

### Inline Code Examples

For inline code blocks, use:

```rst
.. code-block:: http

    GET /authorize?client_id=123&request_uri=urn%3Aietf HTTP/1.1
    Host: example.org
```

Specify the appropriate language for syntax highlighting.

### External Code Files

For larger code examples, store them in separate files (under `examples/` directory) and include them using `literalinclude`:

```rst
.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON
```

Label non-normative examples explicitly in the surrounding text.

## Notes and Warnings

Use note and warning directives to highlight important information:

```rst
.. note::
  This is a note providing additional information.

.. warning::
  This is a warning about potential issues.
```

Notes and warnings should be indented with 2 spaces.

