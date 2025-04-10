using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using FileEndpointRepo;

namespace FileEndPointREST.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FileEndpointController : ControllerBase
    {
        private FileEndpointRepository _fileEndpointRepository;

        public FileEndpointController(FileEndpointRepository fileEndpointRepository)
        {
            _fileEndpointRepository = fileEndpointRepository;
        }

        [HttpGet]
        public IActionResult Get()
        {
            var files = _fileEndpointRepository.GetFileNames();
            return Ok(files);
        }

        [HttpGet("{fileName}")]
        public List<FileEndpoint>? Get(string fileName) 
        {
            return _fileEndpointRepository.GetEndpoints(fileName);
        }
       

        [HttpPost("{fileName}")]
        public FileEndpoint Post(string fileName, [FromBody] FileEndpoint fileEndpoint)
        {
            return _fileEndpointRepository.Add(fileName, fileEndpoint);
        }


        [HttpDelete("{fileName}")]
        public FileEndpoint? Delete(string fileName, [FromBody] FileEndpoint endpointToBeDeleted)
        {
            return _fileEndpointRepository.Delete(fileName, endpointToBeDeleted);
        }

    }
}
