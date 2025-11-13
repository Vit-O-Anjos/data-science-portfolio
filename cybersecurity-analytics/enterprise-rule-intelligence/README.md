# Enterprise Detection Analytics & Rule Intelligence Platform (v5)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-Compatible-blue.svg)](https://code.visualstudio.com/)
[![Google Colab](https://img.shields.io/badge/Google_Colab-Compatible-yellow.svg)](https://colab.research.google.com/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red.svg)](https://attack.mitre.org/)

A universal Python-based analytics platform for analyzing cybersecurity detection rules across multiple security tools and frameworks. Works seamlessly in Colab, Jupyter, and VS Code.

## 🚀 Universal Compatibility

Now supporting all major Python environments:

- ✅ **Google Colab** - Full interactive experience with file uploads
- ✅ **Jupyter Notebook** - Complete functionality with local file access
- ✅ **VS Code** - Full IDE integration with debugging capabilities
- ✅ **JupyterLab** - Advanced notebook interface support

### Multi-Environment Features

| Environment | File Loading | Visualization | Interactive Widgets |
|------------|--------------|---------------|-------------------|
| Google Colab | ✅ Upload widget | ✅ Direct display | ✅ Full support |
| Jupyter Notebook | ✅ Local files | ✅ Direct display | ✅ Full support |
| VS Code | ✅ Local files | ✅ Direct display | ✅ Full support |
| JupyterLab | ✅ Local files | ✅ Direct display | ✅ Full support |

## Overview

This platform provides automated analysis and visualization of detection rules from various security platforms (Snort, YARA, Sigma, Elastic). It parses rule files, maps them to the MITRE ATT&CK framework, and generates detailed analytical visualizations to help security teams understand their detection coverage.

## Key Features

### Universal Rule Parsing

- **Multi-format Support**: Automatically detects and parses Snort/Suricata, YARA, Sigma, and Elastic rule formats
- **Auto-detection**: Intelligently identifies rule format based on content patterns and file extensions
- **MITRE ATT&CK Mapping**: Maps detection rules to 200+ MITRE ATT&CK techniques using pattern matching
- **Feature Engineering**: Extracts detection patterns (network, file, system indicators) and calculates signature characteristics

### Universal Data Loading

- **Smart Auto-detection**: Automatically detects file formats and converts raw rules to analytics-ready format
- **Multi-source Support**: Works with uploaded files (Colab) and local file paths (Jupyter/VS Code)
- **Format Agnostic**: Handles both ready-to-analyze formats and raw rule files with automatic conversion
- **Error Resilient**: Robust error handling for malformed files and format inconsistencies

### Comprehensive Analytics

The platform performs three types of analysis:

1. **Coverage Analysis**
   - MITRE ATT&CK tactic and technique coverage
   - Platform-specific coverage distribution
   - Detection gap identification

2. **Pattern Analysis**
   - Detection pattern utilization (network, file, system indicators)
   - Pattern combination effectiveness
   - Cross-platform pattern comparison

3. **Signature Analysis**
   - Signature length distribution and statistics
   - Complexity metrics
   - Platform-specific characteristics

### Visualization Engine

Generates **30+ professional visualizations** across two dashboard types:

- **Executive Dashboard** (14 visualizations): High-level security posture overview
- **Technical Analysis** (17 visualizations): Detailed analytical charts with comprehensive statistics

## Technical Specifications

- **Language**: Python 3.8+
- **Code Size**: ~450 lines of production-quality code
- **Architecture**: 5-stage modular pipeline with enhanced universal loader
- **Visualization Engine**: 30+ professional charts (14 executive + 17 technical)
- **Data Processing**: Pandas, NumPy with comprehensive feature engineering
- **MITRE Coverage**: 200+ techniques with official STIX/TAXII integration
- **Compatibility**: Universal support for Colab, Jupyter, VS Code, JupyterLab
- **Dependencies**: 10+ carefully selected packages with optional imports

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/detection-analytics-platform.git
cd detection-analytics-platform

# Install required dependencies
pip install pandas matplotlib seaborn numpy ipywidgets
```

**Optional**: For official MITRE ATT&CK data integration:
```bash
pip install attackcti
```

## Usage

### In Google Colab

1. Upload the notebook to Google Colab
2. Run all cells to initialize the platform
3. Click "🚀 Analyze ANY Detection Rules Data"
4. Upload your detection rules file (any supported format)
5. View generated visualizations and reports

### In Jupyter Notebook / VS Code

1. Open the notebook in your preferred environment
2. Run all cells to initialize the platform
3. Use the file path input to analyze local detection rule files
4. View generated visualizations directly in the notebook

### Local File Analysis (Jupyter/VS Code)

```python
# For local file analysis in Jupyter/VS Code
file_path = "/path/to/your/detection_rules.rules"
# The platform automatically detects format and processes the file
```

## Supported File Formats

**Ready-to-Analyze**:
- CSV files with detection rules
- JSON/JSONL rule data
- Parquet analytics data

**Raw Rules (Auto-conversion)**:
- Snort/Suricata rules (`.rules`, `.snort`, `.suricata`)
- YARA rules (`.yar`, `.yara`)
- Sigma rules (`.yml`, `.yaml`)
- Elastic rules (`.json`)
- Generic detection rules (`.txt`, `.conf`)

## Environment-Specific Setup

### Google Colab
- No additional setup required
- File upload via interactive widget
- Direct visualization display

### Jupyter Notebook
```bash
# Start Jupyter
jupyter notebook
# Open detection_analytics_platform.ipynb
```

### VS Code
1. Install Python extension and Jupyter support
2. Open the `.ipynb` file
3. Select Python kernel
4. Run all cells

### JupyterLab
```bash
pip install jupyterlab
jupyter lab
```

## Sample Visualizations

### MITRE ATT&CK Coverage Analysis Suite
Comprehensive three-panel view from the executive dashboard showing tactical coverage, top techniques, and efficiency analysis:

![MITRE Coverage Suite](visualisations/mitre_coverage_suite.png)
*Figure 1: MITRE ATT&CK coverage analysis suite showing tactical distribution, top techniques, and efficiency metrics*

### Rule Type Distribution
Comprehensive analysis of detection methodology distribution with detailed statistics:

![Rule Type Distribution](visualisations/1_rule_type_distribution.png)
*Figure 2: Detection rule type distribution across the security portfolio*

### Platform Utilization
Multi-platform detection capability analysis with performance metrics:

![Platform Utilization](visualisations/2_platform_utilization.png)
*Figure 3: Security platform utilization and capability distribution*

### Detection Pattern Utilization
Pattern extraction and analysis showing network, file, and system indicator usage:

![Detection Patterns](visualisations/7_detection_patterns.png)
*Figure 4: Detection pattern utilization across network, file, and system indicators*

### Cross-Platform Heatmaps
Advanced correlation analysis across platforms, tactics, and threat categories:

![Cross-Platform Heatmaps](visualisations/13_cross_platform_heatmaps.png)
*Figure 5: Cross-platform heatmap analysis showing platform-tactic-threat correlations*

### Compact Strategic Dashboard
Four-panel strategic overview with advanced metrics including outlier detection and capability matrices:

![Compact Strategic Dashboard](visualisations/17_compact_strategic_dashboard.png)
*Figure 6: Compact strategic dashboard with multi-dimensional security metrics*

## 🚀 Live Demo & Complete Output

### 🛠️ Interactive Version (Ready to Run)
- 🎮 [Run in Google Colab](https://colab.research.google.com/github/Vit-O-Anjos/data-science-portfolio_0/blob/main/cybersecurity-analytics/enterprise-rule-intelligence/enterprise_intelligence_platform.ipynb)

**To use sample data:**

**Option 1: Direct Downloads**
- 📄 [snort3.rules](https://raw.githubusercontent.com/Vit-O-Anjos/data-science-portfolio_0/main/cybersecurity-analytics/enterprise-rule-intelligence/data/snort3.rules)
- 📄 [snort3-community.rules](https://raw.githubusercontent.com/Vit-O-Anjos/data-science-portfolio_0/refs/heads/main/cybersecurity-analytics/enterprise-rule-intelligence/data/snort3-community.rules?token=GHSAT0AAAAAADPBRSWEUW7LOEQKHJPPAGHQ2IVWRGQ)
- 📄 [snort2.rules](https://raw.githubusercontent.com/Vit-O-Anjos/data-science-portfolio_0/main/cybersecurity-analytics/enterprise-rule-intelligence/data/snort2.rules)
- 📄 [BLUE_TEAM_DEFENSE_DATASET.jsonl](https://raw.githubusercontent.com/Vit-O-Anjos/data-science-portfolio_0/main/cybersecurity-analytics/enterprise-rule-intelligence/data/BLUE_TEAM_DEFENSE_DATASET.jsonl)

**Option 2: Manual Download**
1. Go to the [`data/`](https://github.com/Vit-O-Anjos/data-science-portfolio_0/tree/main/cybersecurity-analytics/enterprise-rule-intelligence/data) folder
2. Click each file → Click "Download" button
3. Save files to your computer

**Then:**
1. Open the Colab notebook above  
2. Upload the downloaded file when prompted

### 📁 Project Outputs
- 📈 [View Complete Analysis Output](DEMO_OUTPUT.md)
- 🖼️ [All Generated Visualizations](visualisations/)

## Architecture

### Enhanced 5-Stage Analytical Pipeline

#### Stage 1: Universal Rule Converter
- Multi-format parsing with auto-detection
- MITRE ATT&CK mapping (200+ techniques)
- Threat categorization and feature extraction

#### Stage 2: Core Analytics Engine  
- Data validation and quality reporting
- MITRE taxonomy integration
- Advanced feature engineering

#### Stage 3: Comprehensive Analytics Modules
- Coverage Analyzer: MITRE tactic/technique coverage
- Optimization Finder: Statistical analysis
- Pattern Analyzer: Detection pattern effectiveness

#### Stage 4: Professional Visualization Engine
- **Executive Dashboard**: 14 integrated visualizations
- **Technical Analysis**: 23 detailed analytical visualisations

#### Stage 5: Unified Main Engine
- Multi-environment compatibility
- End-to-end workflow automation
- Comprehensive reporting

## Output

The platform generates:

1. **Executive Dashboard**: Single comprehensive image with 14 integrated visualizations
2. **Technical Charts**: 17 detailed analytical visualizations
3. **Reports Directory**: All visualizations saved as high-resolution PNG files (300 DPI)
4. **Console Report**: Statistical summary with key metrics

## MITRE ATT&CK Integration

The platform includes comprehensive MITRE ATT&CK mapping:

- **200+ Technique Mappings**: Covers major ATT&CK techniques and sub-techniques
- **14 Tactical Categories**: Maps to all standard MITRE tactics
- **Pattern-based Detection**: Uses keyword and regex pattern matching
- **Official Data Support**: Optional integration with MITRE STIX/TAXII server via `attackcti` library

## Statistical Analysis Features

Each visualization includes comprehensive statistics:
- Distribution metrics (mean, median, std deviation)
- Coverage percentages and gaps
- Pattern correlations
- Platform-specific characteristics
- Operational insights

## Project Structure

```
enterprise-rule-intelligence/
├── enterprise_intelligence_platform.ipynb
├── README.md
├── DEMO_OUTPUT.md
├── requirements.txt
├── data/
│ ├── snort3.rules
│ ├── snort3-community.rules
│ ├── snort2.rules
│ └── BLUE_TEAM_DEFENSE_DATASET.jsonl
└── visualisations/
  ├── executive_dashboard.png
  ├── mitre_coverage_suite.png
  ├── cross_platform_heatmaps.png
  └── ... (28 additional technical charts)
```

## Technical Approach

### 🔍 Source-First Rule Analysis

The platform specializes in analyzing human-readable source rule files - the format used by detection engineers for development, testing, and optimization. This approach enables:

- **Rule Development Focus**: Analyze rules during creation and refinement phases
- **Cross-Platform Consistency**: Standardized analysis regardless of deployment target
- **Export-Ready Formats**: Compatible with standard export functions from major security platforms

### 🎯 Pattern-Based MITRE ATT&CK Mapping

Uses comprehensive pattern matching against 200+ MITRE techniques, providing:

- **Deterministic Results**: Consistent, reproducible mapping logic
- **Transparent Methodology**: Clear, explainable technique associations
- **High-Performance Processing**: Fast analysis of large rule sets
- **Battle-Tested Coverage**: Proven patterns from real-world detection engineering

### 🌐 Universal Environment Support

Enhanced compatibility features:

- **Smart Environment Detection**: Automatically adapts UI for Colab vs local environments
- **Unified Data Loading**: Single interface for both uploaded files and local paths
- **Consistent Visualization**: Same high-quality outputs across all platforms
- **Robust Error Handling**: Graceful fallbacks for environment-specific limitations

> 💡 **Professional Context**: This methodology aligns with enterprise detection engineering workflows where source rule analysis and deterministic mapping are preferred for auditing and optimization

## Dependencies

**Core Requirements** (required for basic functionality):
- `pandas>=1.5.0`, `numpy>=1.21.0` - Data processing and analysis
- `matplotlib>=3.5.0`, `seaborn>=0.11.0` - Visualization engine
- `ipywidgets>=7.7.0`, `IPython>=8.0.0` - Interactive interface
- `scipy>=1.7.0` - Statistical analysis for enhanced visualizations

**Optional Dependencies** (for extended functionality):
- `attackcti>=0.3.0` - Official MITRE ATT&CK data integration
- `pyarrow>=10.0.0` - Parquet file format support
- `ijson>=3.0.0` - Streamed JSON processing for large files

**Installation Commands**:

```bash
# Complete installation (all features)
pip install pandas matplotlib seaborn numpy ipywidgets scipy pyarrow attackcti

# Minimal installation (core functionality) 
pip install pandas matplotlib seaborn numpy ipywidgets scipy

```

## Troubleshooting

### Common Issues

**File Upload Not Working (Jupyter/VS Code)**
- Use the "Local Path" input field instead of file upload
- Ensure file path is accessible to the notebook environment

**Parquet File Errors**
- Install pyarrow for parquet support: `pip install pyarrow`
- The platform provides clear error messages if parquet support is missing

**Visualization Display Issues**
- Restart kernel and run all cells
- Check matplotlib backend configuration

**MITRE Mapping Errors**
- Install `attackcti` for official data
- Platform falls back to enhanced static mapping

## 📫 Contact & Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/vitor-anjos-33242a107/?skipRedirect=true)  
- 💼 [Portfolio](https://github.com/Vit-O-Anjos/data-science-portfolio)  

## 🙏 Acknowledgments

- MITRE ATT&CK Framework for threat taxonomy
- Security community for rule format documentation

## ⭐ Star This Project

If you find this analysis valuable for security operations, please consider giving it a star! 

[![GitHub stars](https://img.shields.io/github/stars/Vit-O-Anjos/data-science-portfolio?style=social)](https://github.com/Vit-O-Anjos/data-science-portfolio)

> Transform raw detection rules into actionable security intelligence—identify coverage gaps, optimize performance, and make data-driven decisions about your defensive capabilities.

<div align="center">

## 🛡️ Map Your Coverage. Optimize Your Rules. Strengthen Your Defense.

**Enterprise detection analytics for data-driven security engineering**

*Now with universal compatibility: Colab • Jupyter • VS Code*

---

Made with 🏗️ and 🔐 by [Vitor Anjos](https://github.com/Vit-O-Anjos)

</div>
