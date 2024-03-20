import asyncio
import time
from OpenAIProc import OpenAIProc
from PDF_processor import PDFProcessor
import re
import json
import os

class CVAnalyzer:
    def __init__(self, cv_paths):
        self.__cv_paths__ = cv_paths
        self.__reader__ = PDFProcessor(cv_paths)
        self.__chunks_list__ = self.__reader__.text_splitter()
        self.proc = OpenAIProc(self.read_config()['api_key'], self.read_config()['organization_id'])
        self.client = OpenAIProc(self.read_config()['api_key'], self.read_config()['organization_id']).client

    def read_config(self):
        with open('credentials.json') as config_file:
            config = json.load(config_file)
            return config
        
    def get_chunks(self):
        return self.__chunks_list__
    # PROMPT FOR JSON: Give results in the format of json file with folloeing structure: candidate_name, file_name, work_experience, skills
    async def get_work_experience_info(self):
        work_exp_response_of_all_candidates = []
        for cv_index, cv_path in enumerate(self.__cv_paths__):
            prompt = f'Return the result only as the JSON formatted list nothing else with the following data about each file: "candidate_name", "{cv_path}", "total_years_of_experience", "skills_summary_info" with your thoughts about your choosing {cv_index + 1}' # Just a random test prompt
            work_exp_response = await self.proc.openai(self.get_chunks()[cv_index], prompt)
            
            regex_pattern = r"```\s*json\s*(.*?)\s*```"
            result = re.sub(regex_pattern,r"\1", work_exp_response, flags=re.DOTALL)
            work_exp_response_of_all_candidates.append(json.loads(result))

        output_file_path = "/final_result/final_result.json"
        with open(output_file_path, "w") as output_file:
            json.dump(work_exp_response_of_all_candidates, output_file, indent=4)
            print(f"Final result written to {output_file_path}")
        return work_exp_response_of_all_candidates
    

async def analyze_cvs():
    path = "cvs/"
    dir_list = os.listdir(path)
    cv_paths = dir_list
    # def list_pdfs(folder_path):
    #     pdf_paths = []
    #     for root, _, files in os.walk(folder_path):
    #     for filename in files:
    #         if filename.lower().endswith(".pdf"):
    #             pdf_paths.append(os.path.join(root, filename))
    #     return pdf_paths
    cv_paths = [] #massive with pdf's
    analyzer = CVAnalyzer(cv_paths)
    result = await analyzer.get_work_experience_info()
    print(result)

async def main():
    start_time = time.time()
    await analyze_cvs()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Program execution time: {execution_time} seconds")
if __name__ == "__main__":
    print('---------------------------------------------------')
    asyncio.run(main())

# Output: Program execution time: 86.23586583137512 seconds (for 6 PDFs)