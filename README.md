# 🦁 Wildlife Vision

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**AI-powered wildlife analysis platform combining computer vision, data analytics, and LLM capabilities for species identification, conservation insights, and interactive wildlife exploration.**

---

## 🌟 Features

- **🔍 Species Identification**: Upload images and get instant species recognition using state-of-the-art deep learning models
- **📊 Data Explorer**: Interactive data exploration with filters, visualizations, and analytics
- **🌍 Conservation Insights**: Biodiversity metrics, endangered species tracking, and conservation hotspots
- **🖼️ Image Gallery**: Browse wildlife images with quality assessment and filtering
- **💬 Ask Wildlife Expert**: AI-powered chat assistant with RAG for accurate wildlife information
- **🎮 Fun Zone**: Educational quizzes, games, and daily wildlife facts

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip or conda package manager
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/wildlife-vision.git
cd wildlife-vision
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys (for LLM features)
```

5. **Run the application**
```bash
streamlit run Home.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
wildlife-vision/
├── .github/
│   └── workflows/          # CI/CD pipelines
├── data/
│   ├── raw/               # Raw dataset files
│   ├── processed/         # Preprocessed data
│   └── knowledge_base/    # RAG knowledge base
├── models/
│   ├── classification/    # Species identification models
│   ├── quality_assessment/# Image quality models
│   └── embeddings/        # Vector embeddings
├── src/
│   ├── data_processing/   # Data pipeline modules
│   ├── ml_models/         # Model training & inference
│   ├── llm_integration/   # LLM and RAG components
│   └── utils/             # Utility functions
├── pages/
│   ├── 1_Species_Identification.py
│   ├── 2_Data_Explorer.py
│   ├── 3_Conservation_Insights.py
│   ├── 4_Image_Gallery.py
│   ├── 5_Ask_Wildlife_Expert.py
│   └── 6_Fun_Zone.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                  # Documentation
├── Home.py               # Main entry point
├── requirements.txt
└── README.md
```

---

## 🛠️ Development

### Setting up development environment

1. **Install development dependencies**
```bash
pip install -r requirements.txt
```

### Code Quality Standards

- **Code formatting**: Black (line length 88)
- **Linting**: Flake8
- **Type checking**: MyPy
- **Testing**: Pytest with >80% coverage
- **Security**: Bandit for security checks

---

## 📊 Current Sprint: Sprint 0

**Goal**: Foundation & Setup

**Status**: 🟢 In Progress

### Sprint 0 Tasks
- [x] Create GitHub repository
- [x] Set up project structure
- [x] Create requirements.txt
- [x] Configure .gitignore
- [x] Write initial README
- [ ] Install and explore wildlife_datasets
- [ ] Set up CI/CD pipeline
- [ ] Configure pre-commit hooks
- [ ] Create basic home page
- [ ] Deploy initial version

---

## 🚢 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set environment variables in Streamlit Cloud dashboard
5. Deploy!

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/sprint-1-species-id`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add species identification'`)
6. Push to the branch (`git push origin feature/sprint-1-species-id`)
7. Open a Pull Request

### Pull Request Requirements

- ✅ All CI checks pass
- ✅ Code review approved
- ✅ Test coverage ≥80%
- ✅ Documentation updated
- ✅ No merge conflicts

---

## 🔧 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.10+
- **ML/DL**: PyTorch, torchvision, timm
- **Data**: pandas, numpy, wildlife_datasets
- **Visualization**: Plotly, Matplotlib, Folium
- **LLM**: Ollama, LangChain, Google's Gemini
- **Vector DB**: ChromaDB/FAISS
- **CI/CD**: GitHub Actions
- **Deployment**: Streamlit Cloud

---

## 📈 Roadmap

### Current Sprint
- ✅ Sprint 0: Foundation & Setup (Week 1-2)

### Upcoming Sprints
- 🔄 Sprint 1: Species Identification (Week 3-4)
- ⏳ Sprint 2: Data Explorer (Week 5-6)
- ⏳ Sprint 3: Image Gallery (Week 7-8)
- ⏳ Sprint 4: LLM Integration (Week 9-10)
- ⏳ Sprint 5: Ask Wildlife Expert (Week 11-12)
- ⏳ Sprint 6: Conservation Insights (Week 13-14)
- ⏳ Sprint 7: Fun Zone (Week 15-16)
- ⏳ Sprint 8: Polish & Advanced Features (Week 17-18)
- ⏳ Sprint 9: Testing & Documentation (Week 19-20)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **wildlife_datasets** - Core dataset package
- **Streamlit** - Amazing web framework
- **PyTorch** - Deep learning framework
- **LangChain** - LLM application framework
- Conservation organizations and wildlife photographers

---

## 📧 Contact

- **Project Maintainer**: [Sohan Puthran]
- **Email**: [puthran.sohan@gmail.com]
- **GitHub**: [@sohansputhran](https://github.com/sohansputhran)
- **Project Link**: [https://github.com/sohansputhran/wildlife-vision](https://github.com/sohansputhran/wildlife-vision)

---

## 🌱 Support Wildlife Conservation

This project is dedicated to wildlife conservation. Consider supporting:
- [World Wildlife Fund](https://www.worldwildlife.org/)
- [Wildlife Conservation Society](https://www.wcs.org/)
- [International Union for Conservation of Nature](https://www.iucn.org/)

---

**Built with ❤️ for wildlife conservation**
