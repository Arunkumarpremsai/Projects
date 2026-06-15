import streamlit as st
import ollama
import os
import tempfile
import pymupdf4llm

# ==========================================
# CONFIGURATION & SETUP
# ==========================================
st.set_page_config(page_title="AI Due Diligence Copilot", page_icon="💼", layout="wide")

st.sidebar.info("🤖 Using Local Ollama Instance for Privacy-Preserving Analysis")

# ==========================================
# SYSTEM PROMPT (From User Definition)
# ==========================================
DUE_DILIGENCE_SYSTEM_PROMPT = """
You are an elite AI Due Diligence Copilot designed for investment firms, private equity funds, venture capital firms, corporate development teams, M&A advisors, consulting firms, auditors, and financial analysts.
Your primary objective is to accelerate due diligence by extracting, analyzing, validating, and synthesizing information from multiple business documents while maintaining the highest standards of accuracy, transparency, and traceability.

Operating Principles:
1. Evidence First: Never make assumptions. Every conclusion must be supported by evidence extracted from provided documents. Format:
   Evidence: [Direct Extract] | Source: Document Name, Page | Confidence: High/Medium/Low
2. Executive-Level Communication: Present findings in a concise, professional, boardroom-ready format using bullet points, tables, and risk summaries. Avoid unnecessary jargon.
3. Cross-Document Validation: Compare findings across documents, identify inconsistencies, flag contradictions, and highlight missing information.

Output Structure (ALWAYS return results in this exact order):
1. Executive Summary (Investment Snapshot, Highlights, Risks, Overall Assessment Score 0-100)
2. Company Overview
3. Financial Analysis
4. Risk Assessment
5. Growth Opportunities
6. Competitive Analysis
7. Management Assessment
8. Due Diligence Red Flags
9. Open Questions
10. Recommended Next Steps

Confidence and Transparency Rules:
For every major conclusion provide:
Confidence Score: 0-100%
Reasoning: Short explanation.
Evidence: Source citation.
Never fabricate information. If information is unavailable state: "Insufficient evidence available to support a conclusion."

Behavioral Instructions:
You act like a hybrid of a McKinsey Consultant, Goldman Sachs Analyst, and Big Four Transaction Advisory Expert. Prioritize accuracy, explainability, traceability, and business impact.
"""

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def chunk_markdown(text, chunk_size=4000, overlap=500):
    """Splits markdown text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def extract_and_chunk_pdfs(uploaded_files, chunk_size=4000, overlap=500):
    """Saves uploaded PDFs temporarily, converts to Markdown, and chunks the text."""
    all_chunks_formatted = ""
    chunk_counter = 1
    
    for file in uploaded_files:
        all_chunks_formatted += f"\n\n{'='*40}\nSTART OF DOCUMENT: {file.name}\n{'='*40}\n\n"
        
        # Streamlit files are in memory. We must write to a temp file for pymupdf4llm
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(file.read())
            temp_pdf_path = temp_pdf.name

        try:
            # Convert PDF directly to Markdown (preserves tables and headers beautifully)
            md_text = pymupdf4llm.to_markdown(temp_pdf_path)
            
            # Chunk the resulting markdown
            document_chunks = chunk_markdown(md_text, chunk_size, overlap)
            
            for i, chunk in enumerate(document_chunks):
                all_chunks_formatted += f"\n\n--- [Doc: {file.name} | Chunk {i+1}/{len(document_chunks)}] ---\n"
                all_chunks_formatted += chunk
                chunk_counter += 1
                
        except Exception as e:
            all_chunks_formatted += f"\n[Error processing {file.name}: {str(e)}]\n"
        finally:
            # Clean up the temporary file securely
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
                
        all_chunks_formatted += f"\n\n{'='*40}\nEND OF DOCUMENT: {file.name}\n{'='*40}\n\n"
        
    return all_chunks_formatted

def generate_due_diligence_report(context_text, specific_query="", model_name="llama3"):
    """Calls local Ollama with the system prompt and document context."""
    
    prompt = f"""
    Please perform a comprehensive due diligence analysis based ONLY on the following provided documents.
    Adhere strictly to the requested Output Structure and Operating Principles.
    
    If the user has a specific focus or query, address it here: {specific_query}
    
    DOCUMENTS CONTEXT:
    {context_text}
    """
    
    messages = [
        {"role": "system", "content": DUE_DILIGENCE_SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
    
    with st.spinner(f"Analyzing documents and generating report via Ollama ({model_name}). This may take a while depending on your hardware and context length..."):
        try:
            response = ollama.chat(model=model_name, messages=messages)
            return response['message']['content']
        except Exception as e:
            raise Exception(f"Ollama Error: {str(e)}. Ensure Ollama is running (`ollama serve`) and the model '{model_name}' is downloaded (`ollama run {model_name}`).")

# ==========================================
# STREAMLIT UI
# ==========================================
def main():
    st.title("💼 AI Due Diligence Copilot")
    st.markdown("Upload target company documents (Annual Reports, Pitch Decks, Financials) to generate an institutional-grade due diligence report.")

    # Sidebar for inputs
    with st.sidebar:
        st.header("⚙️ Configuration")
        ollama_model = st.text_input(
            "Ollama Model Name", 
            value="qwen3:32b", 
            help="Ensure you have pulled this model locally using `ollama run <model_name>`."
        )
        
        st.header("1. Upload Documents")
        uploaded_files = st.file_uploader(
            "Upload PDFs (e.g., 10-K, Pitch Deck, Audited Financials)", 
            type=["pdf"], 
            accept_multiple_files=True
        )
        
        st.header("2. Analysis Focus (Optional)")
        specific_query = st.text_area(
            "Specific areas to focus on?", 
            placeholder="e.g., Pay special attention to customer concentration risks in the SaaS segment."
        )
        
        analyze_button = st.button("Generate DD Report", type="primary", use_container_width=True)

    # Main content area
    if analyze_button:
        if not uploaded_files:
            st.error("Please upload at least one document to begin analysis.")
        else:
            # 1. Extract and Chunk Text
            st.info(f"Converting {len(uploaded_files)} document(s) to Markdown and chunking...")
            document_context = extract_and_chunk_pdfs(uploaded_files, chunk_size=4000, overlap=500)
            
            # 2. Check context length (Basic safeguard)
            if len(document_context) < 50:
                st.error("Could not extract sufficient text from the provided documents. Please ensure they are readable PDFs.")
                return

            # 3. Generate Report
            try:
                report = generate_due_diligence_report(document_context, specific_query, ollama_model)
                
                # 4. Display Report
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(report)
                
                # Option to download
                st.download_button(
                    label="Download Report as TXT",
                    data=report,
                    file_name="Due_Diligence_Report.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred during communication with Ollama: {str(e)}")

if __name__ == "__main__":
    main()