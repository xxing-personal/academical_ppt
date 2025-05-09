import { useState } from 'react';
import FileUpload from './components/FileUpload';

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileSelect = (file: File) => {
    setSelectedFile(file);
    // Here you can add additional logic like uploading the file to the backend
    console.log('Selected file:', file.name);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div className="relative py-3 sm:max-w-xl sm:mx-auto">
        <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div className="max-w-md mx-auto">
            <div className="divide-y divide-gray-200">
              <div className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                <h1 className="text-3xl font-bold text-center text-gray-900 mb-8">
                  Academical PPT
                </h1>
                <FileUpload onFileSelect={handleFileSelect} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
