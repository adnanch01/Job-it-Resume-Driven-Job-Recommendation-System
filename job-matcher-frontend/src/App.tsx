import ResumeUpload from './components/ResumeUpload';

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-8">
      <h1 className="text-4xl font-bold mb-4">Job Matcher</h1>
      <p className="text-lg text-gray-300 mb-8 text-center max-w-xl">
        Upload your resume and we'll match it to jobs based on your skills using NLP.
      </p>

      <ResumeUpload />
    </div>
  );
}

export default App;
