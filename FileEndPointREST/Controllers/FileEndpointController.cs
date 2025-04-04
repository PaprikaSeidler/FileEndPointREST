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
        public IActionResult GetFiles()
        {
            var files = _fileEndpointRepository.GetFileNames();
            return Ok(files);
        }
    }
}
