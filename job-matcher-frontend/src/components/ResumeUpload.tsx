import { useState } from 'react';
import axios from 'axios';

const ResumeUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [parsed, setParsed] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('resume', file);
    try {
      setLoading(true);
      const res = await axios.post('http://127.0.0.1:5000/upload-resume', formData);
      setParsed(res.data);
    } catch (err) {
      alert('Failed to upload resume');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-gray-800 p-6 rounded-lg shadow-md w-full max-w-xl">
      <h2 className="text-2xl font-semibold mb-4">Upload Resume</h2>
      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="block w-full mb-4 bg-gray-700 text-white p-2 rounded"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        disabled={!file || loading}
      >
        {loading ? 'Uploading...' : 'Upload & Parse'}
      </button>

      {parsed && (
        <div className="mt-6 text-left">
          <h3 className="text-xl font-bold mb-2">Parsed Skills:</h3>
          <ul className="list-disc list-inside text-green-300">
            {parsed.skills.map((skill: string, i: number) => (
              <li key={i}>{skill}</li>
            ))}
          </ul>

          <h3 className="text-xl font-bold mt-4 mb-2">Experience Section:</h3>
          <p className="text-gray-300 whitespace-pre-line">{parsed.experience || 'No experience section found.'}</p>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
