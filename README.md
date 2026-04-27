# FairLens - AI Bias Detector

**Problem**: Banks and NBFCs use AI for loan approvals but models often discriminate by gender and age, violating fairness norms like the EU AI Act. This creates financial exclusion and legal risk.

**Solution**: FairLens is a no-code web tool that scans any AI model CSV and flags bias in 30 seconds. It generates a PDF audit report with risk scores and actionable fixes for developers and auditors.

![Demo Chart](bias_chart.png)

**Demo Results**: 
- **Gender Bias Score**: 0.37 = HIGH RISK | Approval Rate: Female 23.5% vs Male 60.7%
- **Age Bias Score**: 0.13 = HIGH RISK | Approval Rate: Old 42.0% vs Young 55.1%
- **Compliance Check**: Fails EU AI Act threshold of 0.10 on both metrics

**Key Features**:
1. **30-Second Scan**: Upload CSV → Get bias report. No ML expertise needed.
2. **Actionable PDF**: Not just metrics. Includes specific fixes like "Rebalance training data for Female applicants".
3. **Multi-Metric**: Checks Gender, Age, and custom sensitive attributes using Fairlearn.
4. **No-Code**: Built for students, NGOs, and NBFC auditors — not just engineers.

**How to Run Locally**:
```bash
git clone https://github.com/Ragini1111/fairlens
cd fairlens
pip install pandas fairlearn matplotlib scikit-learn
python bias_check.py
```
**Core Tech Stack**: Python, Pandas, Fairlearn, Scikit-learn, Matplotlib, Next.js, React, Tailwind CSS
**Deployment**: Vercel
**Built for**: Google Solution Challenge 2026 | UN SDG 10: Reduced Inequalities  Live Demo: https://v0-fairscan-ai-bias.vercel.app
**Demo Video**: [Add your 3-min YouTube link here]

---

### Development Workflow
**Development Environment**: GitHub Codespaces  
**AI-Assisted Development**: Leveraged Gemini CLI and Claude during development for rapid prototyping, debugging, and documentation  

*Note: The final FairLens application runs entirely on open-source Python libraries. No third-party AI API calls are required for the core bias detection functionality.*
